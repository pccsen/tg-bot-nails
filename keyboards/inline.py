from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import AVAILABLE_TIMES

service_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Маникюр", callback_data="category_manicure")],
    [InlineKeyboardButton(text="Ресницы", callback_data="category_lashes")],
    [InlineKeyboardButton(text="Брови", callback_data="category_brows")],
])

time_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=time, callback_data=f"time_{time}")] for time in AVAILABLE_TIMES]
)

master_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Айлина Мажетова", callback_data="master_Айлина")],
    [InlineKeyboardButton(text="Каусар Сарагелдин", callback_data="master_Каусар")],
    [InlineKeyboardButton(text="Анна Русланова", callback_data="master_Анна")],
    [InlineKeyboardButton(text="Роза Салатова", callback_data="master_Роза")],
])

svobodnie_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Айлина Мажетова", callback_data="master_Айлина")],
])

zapis_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Записаться", callback_data="zapisat_sya")]
])

portfolio_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📸 Портфолио мастеров", url="https://drive.google.com/file/d/1ETneS9yTNF3PbVWHOVR540x6eiVR247c/view?usp=share_link")]
])