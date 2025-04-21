from aiogram import Router, types, F

router = Router()

@router.message(F.text == "Контакты")
async def contacts_handler(message: types.Message):
    await message.answer("📞 Наши контакты:\n\n+7 707 745 7608\n@aikunaaa04")
