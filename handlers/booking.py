from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from states.booking_state import BookingState
from keyboards.inline import time_keyboard, master_keyboard
from database.db import cursor, conn
from datetime import datetime

router = Router()

# Начало бронирования по выбору категории
@router.callback_query(lambda c: c.data.startswith("category_"))
async def start_booking(callback: CallbackQuery, state: FSMContext):
    category = callback.data.split("_")[1]
    await state.update_data(category=category)  # сохраняем категорию
    await state.set_state(BookingState.name)
    await callback.message.answer(f"Вы выбрали: {category.capitalize()}\nВведите ваше имя:")

# Ввод имени
@router.message(BookingState.name)
async def booking_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookingState.phone)
    await message.answer("Введите номер телефона:")

# Ввод номера телефона
@router.message(BookingState.phone)
async def booking_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(BookingState.date)
    await message.answer("Введите дату (ДД.ММ.ГГГГ):")

# Ввод даты
@router.message(BookingState.date)
async def booking_date(message: types.Message, state: FSMContext):
    try:
        datetime.strptime(message.text, "%d.%m.%Y")
        await state.update_data(date=message.text)
        await state.set_state(BookingState.time)
        await message.answer("Выберите время:", reply_markup=time_keyboard)
    except ValueError:
        await message.answer("Неверный формат даты! Пожалуйста, введите в формате ДД.ММ.ГГГГ.")

# Выбор времени
@router.callback_query(lambda c: c.data.startswith("time_"))
async def booking_time(callback: CallbackQuery, state: FSMContext):
    await state.update_data(time=callback.data.split("_")[1])
    await state.set_state(BookingState.master)
    await callback.message.answer("Выберите мастера:", reply_markup=master_keyboard)

# Выбор мастера и сохранение записи
@router.callback_query(lambda c: c.data.startswith("master_"))
async def booking_master(callback: CallbackQuery, state: FSMContext):
    master = callback.data.split("_")[1]
    await state.update_data(master=master)
    data = await state.get_data()
    cursor.execute(
        "INSERT INTO appointments (user_id, name, phone, date, time, master) VALUES (?, ?, ?, ?, ?, ?)",
        (callback.from_user.id, data['name'], data['phone'], data['date'], data['time'], data['master'])
    )
    conn.commit()
    await callback.message.answer(
        f"Вы успешно записаны!\n\n📅 Дата: {data['date']}\n⏰ Время: {data['time']}\n💇 Мастер: {data['master']}"
    )
    await state.clear()
