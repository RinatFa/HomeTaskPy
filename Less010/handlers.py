from main import bot, dp  # не создавать dp, а получать из main
import time     
from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text
from config import admin_id
from config import BANK

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен\n \
    /help, /start, /game, /quit")
# После запуска main в чате мне сообщение "Бот запущен"

MSG2 = "{}, /start - начать игру\n \
    /game - играть\n \
    /quit - выход из игры"
@dp.message_handler(commands=['help'])             #r команда
async def start_handler(message: types.Message):
    user_id = message.from_user.id                  #r число
    user_name = message.from_user.first_name        #r Имя
    await bot.send_message(user_id, MSG2.format(user_name))

MSG = "{}, выберите действие:"                      #r Имя, действие

@dp.message_handler(commands=['start'])             #r команда старт /start
async def start_handler(message: types.Message):
    user_id = message.from_user.id                  #r число
    user_name = message.from_user.first_name        #r Имя
    await message.reply(f"Hi, {user_name}!\n \
        Меню:\n \
        /game - играть, повтор игры\n \
        /quit - выход из игры") 
    time.sleep(1)                                   
    btns = types.ReplyKeyboardMarkup(row_width=2)   #r две кнопки в ширину
    btn_calc = types.KeyboardButton('/game')        #r кнопка Игра
    btn_out = types.KeyboardButton('/quit')         #r кнопка Выход
    btns.add(btn_calc, btn_out)                     #r добавление кнопок
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)
        #r Передача сообщения от бота: Имя, действие и панель кнопок

@dp.message_handler(commands=['game'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Я открываю игру")
    global iBank
    iBank = BANK
    value = "100"
    if value == "":
        await bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, value, reply_markup=keyboard)

iBank = BANK
@dp.callback_query_handler(lambda c: True)
async def callback_calc(query):

    global value, old_value, iBank
    data = query.data

    if data == "=":
        try:
            valueSub = str(iBank) + "-" + value
            iBank = iBank - int(value)
            value = str(eval(valueSub))  #r вычисление
            if int(value) > 0:
                value = "осталось " + value + " конфет"
            else:
                value = "конфеты закончились!"
        except:
            value = "Error"
    else:
        if len(value) < 3:
            value += data  # добавляет цифры к числу
        elif value[:3] == "Вве":
            value = ""
            value += data
        else:
            value = "Введите число!"

    if (value != old_value and value != "") or ("0" != old_value and value == ""):
        if value == "":
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text="0", reply_markup=keyboard)
            old_value = "0"     # reply_markup=keyboard - перерисовка всех кнопок
        else:
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text=value, reply_markup=keyboard)
                                # reply_markup=keyboard - перерисовка всех кнопок
            old_value = value

    if value == "Error":
        value = ""

@dp.message_handler(commands=['quit'])              #r команда выход
async def quit_handler(message: types.Message):     
    await bot.send_message(message.from_user.id, 'До свидания! Увидимся...',
                           reply_markup=types.ReplyKeyboardRemove())
        #r сообщение от бота, закрытие панели кнопок
value = ""
old_value = ""
keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard.row(types.InlineKeyboardButton(" 1 ", callback_data="1"),
             types.InlineKeyboardButton(" 2 ", callback_data="2"),
             types.InlineKeyboardButton(" 3 ", callback_data="3"))
keyboard.row(types.InlineKeyboardButton(" 4 ", callback_data="4"),
             types.InlineKeyboardButton(" 5 ", callback_data="5"),
             types.InlineKeyboardButton(" 6 ", callback_data="6"))
keyboard.row(types.InlineKeyboardButton(" 7 ", callback_data="7"),
             types.InlineKeyboardButton(" 8 ", callback_data="8"),
             types.InlineKeyboardButton(" 9 ", callback_data="9"))
keyboard.row(types.InlineKeyboardButton(" 0 ", callback_data="0"),
             types.InlineKeyboardButton(" ход ", callback_data="="))
