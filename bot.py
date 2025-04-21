from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from handlers import start, services, booking, location, contacts
from utils.notify import send_notifications
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Роутерлер старт сервис локация деген сиякты
for router in (start.router, services.router, booking.router, location.router, contacts.router):
    dp.include_router(router)

async def main():
    asyncio.create_task(send_notifications(bot))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())