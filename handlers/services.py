from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from keyboards.inline import service_menu
from states.booking_state import BookingState

router = Router()

@router.message(F.text == "Записаться")
async def services_handler(message: types.Message):
    await message.answer(
        "💇‍♀️ Наши услуги:\n- Маникюр\n- Ресницы\n- Брови\n\n👩‍🎨 Выберите категорию:",
        reply_markup=service_menu
    )

@router.callback_query(F.data.startswith("category_"))
async def handle_category(callback: types.CallbackQuery, state: FSMContext):
    category = callback.data.split("_")[1]
    
    # Сохраняем выбранную категорию
    await state.update_data(category=category)

    # Переход к шагу ввода имени
    await state.set_state(BookingState.name)

    await callback.message.answer(f"Вы выбрали: {category.capitalize()}\nВведите ваше имя:")
    await callback.answer()  # Ответ для подтверждения
