from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Записаться")],
        [KeyboardButton(text="Мои записи")],
        [KeyboardButton(text="Где мы")],
        [KeyboardButton(text="Контакты")],
    ],
    resize_keyboard=True
)
