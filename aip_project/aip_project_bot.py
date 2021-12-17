import telebot
import config
import sqlite3

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
connect = sqlite3.connect("project.db", check_same_thread=False)
cursor = connect.cursor()

# Приветствие с пользователями
@bot.message_handler(commands=['start'])
def welcome(message):
    welc = open('welc.webp', 'rb')
    bot.send_sticker(message.chat.id, welc)

    # Клавиатура в чате
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Набрать вес 🍔")
    item2 = types.KeyboardButton("Сбросить вес 🥒")
    item3 = types.KeyboardButton("Узнать каллорийность 👍")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, который поможет тебе подсчитать калории, а также тут ещё много разных плюшек!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, "Скажи, какую преследуешь цель?")

@bot.message_handler(content_types=['text'])
def funcs(message):
    if message.chat.type == 'private':
        if message.text == "Набрать вес 🍔" or message.text == "Сбросить вес 🥒" :

            # Кнопки под сообщением
            InlKey = types.InlineKeyboardMarkup(row_width=2)
            man = types.InlineKeyboardButton("М", callback_data='male')
            woman = types.InlineKeyboardButton("Ж", callback_data='female')

            InlKey.add(man, woman)

            bot.send_message(message.chat.id, "Какой пол? - М/Ж", reply_markup=InlKey)

        elif message.text == 'Узнать каллорийность 👍':
            bot.send_message(message.chat.id,'Введи продукт. Например, "Авокадо":')
        #elif message.text == "Авокадо":
            #bot.send_message(message.chat.id,"<b>Авокадо</b>\n<b>Калории на 100 продукта</b>: 212\n<b>Белки</b>: 2.0\n<b>Жиры</b>: 20.0\n<b>Углеводы</b>: 6.0".format(message.from_user, bot.get_me()),
    #parse_mode='html')
        else:
            bot.send_message(message.chat.id,'Меня ещё не дописали друг, не понимаю тебя.')

def find(message):
    text = message.text
    #print(cursor.execute("SELECT category FROM products WHERE category=?", (text,)))
    cursor.execute("SELECT * FROM products WHERE name LIKE '%'||?||'%'", (text,))
    ans = cursor.fetchall()
    #print(len(ans))
    if len(ans) == 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("Узнать каллорийность 👍",)
        markup.add(item)
        bot.send_message(message.chat.id, 'Таково у нас не водится, попробуй ещё раз', reply_markup=markup)
        bot.register_next_step_handler(message, select_aim)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i, r in enumerate(ans):
            item = types.KeyboardButton(r[2])
            markup.add(item)
        bot.send_message(message.chat.id, "Что именно тебя интересует?", reply_markup=markup)
        bot.register_next_step_handler(message, output)


def output(message):
    text = message.text
    cursor.execute("SELECT energy FROM products WHERE name=?", (text,))
    ans = cursor.fetchone()
    out = text + "\nНа 100 грамм: \n" + str(ans)[2:-3]
    bot.send_message(message.chat.id, out,reply_markup=None)

# Входные данные для бота, с помощью которых будет производиться расчёт. Пока что здесь константы:

# bot.send_message(message.chat.id, "Введи вес:")
weight = 80
# bot.send_message(message.chat.id, "Введи рост:")
height = 180
# bot.send_message(message.chat.id, "Введи возраст:")
age = 20
menform = 88.36 + 13.4 * weight + 4.8 * height - 5.7 * age
womform = 447.6 + 9.2 * weight + 3.1 * height - 4.3 * age


# Ф-ция для кнопок под сообщением
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'male':
                bot.send_message(call.message.chat.id, "Ваша норма калорий составляет: " + str(menform))
            elif call.data == 'female':
                bot.send_message(call.message.chat.id, "Ваша норма калорий составляет: " + str(womform))
    except Exception as e:
        print(repr(e))
# RUN
bot.polling(none_stop=True)
