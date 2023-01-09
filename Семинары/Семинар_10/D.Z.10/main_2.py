import telebot
import random

token = '5942313125:AAE5H3734npJfa-_DBTgxaJYZ7CqyEePcJw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start']) # /start
def welcom(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = telebot.types.KeyboardButton("Знак задиака")
    item_2 = telebot.types.KeyboardButton('угадайка')
    markup.add(item_1, item_2)
    bot.send_message(message.chat.id, "Выбирай", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def f(mess):
    if mess.text == 'Знак задиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item_1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        item_2 = telebot.types.InlineKeyboardButton('телец', callback_data='телец')
        item_3 = telebot.types.InlineKeyboardButton('блзнецы', callback_data='блзнецы')
        item_4 = telebot.types.InlineKeyboardButton('рак', callback_data='рак')
        item_5 = telebot.types.InlineKeyboardButton('лев', callback_data='лев')
        item_6 = telebot.types.InlineKeyboardButton('дева', callback_data='дева')
        item_7 = telebot.types.InlineKeyboardButton('весы', callback_data='весы')
        item_8 = telebot.types.InlineKeyboardButton('скроп', callback_data='скроп')
        item_9 = telebot.types.InlineKeyboardButton('стрелец', callback_data='стрелец')
        item_10 = telebot.types.InlineKeyboardButton('козерог', callback_data='козерог')
        item_11 = telebot.types.InlineKeyboardButton('водолей', callback_data='водолей')
        item_12 = telebot.types.InlineKeyboardButton('рыбы', callback_data='рыбы')
        markup.add(item_1, item_2, item_3, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12)
        bot.send_message(mess.chat.id, 'Отлично, нажимай!?', reply_markup=markup)
    if mess.text == 'угадайка':
        msg = bot.send_message(mess.chat.id, "я загадал число от 1 до 5, попробуй угадай")
        bot.register_next_step_handler(msg, num_rnd)





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    dikt_znak = znak_har()
    if call.data == 'Овен':
        bot.send_message(call.message.chat.id, dikt_znak["Овен"] )
    elif call.data == 'телец':
        bot.send_message(call.message.chat.id, dikt_znak["телец"])
    elif call.data == 'блзнецы':
        bot.send_message(call.message.chat.id, dikt_znak["блзнецы"])

def znak_har():
    dict = {}
    with open('text.txt', 'r', encoding='utf-8') as file:
         for i in range(3):
            str1 = file.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
    return dict


def num_rnd(messag):
    x = random.randint(0, 5)
    print(x)
    if messag.text == str(x):
        bot.send_message(messag.chat.id, f'угадал моё число {x}, молодец')
    else:
        bot.send_message(messag.chat.id, 'не угодал')






bot.polling(non_stop=True)