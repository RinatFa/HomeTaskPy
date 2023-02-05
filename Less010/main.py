import asyncio  # для асинхронных функций, функции async, методы await 

from aiogram import Bot, Dispatcher, executor
# Bot - класс bot, Dispatcher - доставщик Updates, executor - запуск botа
from config import BOT_TOKEN

loop = asyncio.get_event_loop()  # поток для событий
bot = Bot(BOT_TOKEN, parse_mode="HTML")  # создается класс с форматом HTML
dp = Dispatcher(bot, loop=loop)  # обработчик и доставщик, бот и поток

if __name__ == "__main__":  # если имя main
    from handlers import dp, send_to_admin
    print('server start')
    executor.start_polling(dp, on_startup=send_to_admin)
