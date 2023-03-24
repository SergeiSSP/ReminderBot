import os
from datetime import datetime
from time import sleep

from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['remind'])
async def remind(message: types.Message):
    time, text = message.text.split(maxsplit=2)[1:]
    await message.answer(f"Ok, I'll remind you about {text} at {time}")
    while True:
        if current_time().split(':') == time.split(':'):
            await message.answer(f"Reminder: {text}")
            break
        else:
            sleep(5)
            print(current_time())
            continue


def current_time():
    c_t = datetime.now().strftime('%H:%M')
    return c_t


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
