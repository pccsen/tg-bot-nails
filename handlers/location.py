from aiogram import Router, types, F

router = Router()

@router.message(F.text == "Где мы")
async def where_are_we(message: types.Message):
    await message.answer("📍 Мы находимся по адресу: г. Алматы, ул. Сатпаева, 22")
