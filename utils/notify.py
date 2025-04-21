from datetime import datetime, timedelta
from database.db import cursor
import asyncio

async def send_notifications(bot):
    while True:
        now = datetime.now().strftime("%d.%m.%Y %H:%M")
        cursor.execute("SELECT user_id, date, time FROM appointments")
        for user_id, date, time in cursor.fetchall():
            appt_time = datetime.strptime(f"{date} {time}", "%d.%m.%Y %H:%M")
            # Напоминание за 1 час до записи
            if now == (appt_time - timedelta(hours=1)).strftime("%d.%m.%Y %H:%M"):
                await bot.send_message(user_id, f"Напоминание: через 1 час запись в {time}!")
            # Напоминание за 1 день до записи
            if now == (appt_time - timedelta(days=1)).strftime("%d.%m.%Y %H:%M"):
                await bot.send_message(user_id, f"Напоминание: завтра запись в {time}!")
        await asyncio.sleep(60)  # Пауза 60 секунд перед следующей проверкой
