from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from database.db import cursor
from keyboards.reply import main_menu
from keyboards.inline import zapis_keyboard, portfolio_button

router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "🌸 Добро пожаловать в WelcomeTheBeautyHaven 🌸\n\n"
        "Мы рады видеть вас в нашем бьюти-пространстве! ✨\n"
        "Здесь вы можете легко записаться к мастерам на процедуры:\n"
        "💅 Маникюр и педикюр\n👁 Наращивание ресниц\n🌿 Ламинирование и коррекция бровей\n\n"
        "📅 Наши мастера работают ежедневно с 09:00 до 20:00\n🍵 Обед: 13:00 – 14:00",
        reply_markup=main_menu
    )
    await message.answer(
        "📸 Хотите посмотреть примеры работ наших мастеров?",
        reply_markup=portfolio_button
    )

@router.message(F.text == "Мои записи")
async def my_appointments(message: types.Message):
    user_id = message.from_user.id

    # Проверяем, есть ли у пользователя записи
    cursor.execute("SELECT date, time, master FROM appointments WHERE user_id = ?", (user_id,))
    appointments = cursor.fetchall()

    if appointments:
        # Если записи есть, выводим их
        appointment_text = "Ваши записи:\n"
        for appt in appointments:
            appointment_text += f"📅 Дата: {appt[0]}\n⏰ Время: {appt[1]}\n💇 Мастер: {appt[2]}\n\n"
        await message.answer(appointment_text)
    else:
        # Если записей нет
        await message.answer("Вы еще не записывались. Пожалуйста, выберите услугу для записи.", reply_markup=zapis_keyboard)
