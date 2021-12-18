import telebot
import config
import sqlite3

from telebot import types

"""
Этот бот является итоговым проектом по дисциплине "Алгоритмизация и программирование".
Бот создан:
студентами группы БИБ215
Каримовым Каримом 
Чиняевой Алиной

Функция welcome; Функция funcs; Функция get_parms; Функция product_name; Функция router; Функция callback_inline - Каримов Карим 
Файл sql_database.py; База данных "project.db"; Файлы, находящиеся в папке "parcers"; Функция поиска позиций; Функция вывода хараткеристик  - Чиняева Алина

Для изучения использовались материалы:

"""

bot = telebot.TeleBot(config.TOKEN)
connect = sqlite3.connect("project.db", check_same_thread=False)
cursor = connect.cursor()

# Создаём глобальные переменные
m = 0
w = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    """Стартовая функция для бота, приветствует пользователя и предлагает ознакомиться со всеми его функциями."""
    welc = open('welc.webp', 'rb')
    bot.send_sticker(message.chat.id, welc)

    # Клавиатура в чате
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Узнать норму калорий 🍔")
    item2 = types.KeyboardButton("Узнать каллорийность 👍")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, который поможет тебе подсчитать калории, а также тут ещё много разных плюшек!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, "Скажи, какую преследуешь цель?")

@bot.message_handler(content_types=['text'])
def funcs(message):
    """Функция отвечает за выбор пользователя,
       хочет ли он узнать норму калорий или высчитать калорийность продукта,
       при том или ином выборе, происходит перенаправление на отдельные функции
       """
    if message.chat.type == 'private':
        if message.text == "Узнать норму калорий 🍔":

            bot.send_message(message.chat.id, "Укажите ваши параметры Вес, Рост и Возраст в формате: \n'Веc Рост Возраст'")
            bot.register_next_step_handler(message, get_parms)

        elif message.text == 'Узнать каллорийность 👍':
            bot.send_message(message.chat.id,'Введи продукт. Например, "Авокадо":')
            bot.register_next_step_handler(message, find)
        else:
            bot.send_message(message.chat.id,'Не понимаю вас.')

def get_parms(message):
    """Функция отвечает за рассчёт параметров  пользователя, с помощью которых будет производиться расчёт"""
    global m,w
    arr = []
    data = message.text + " "
    ind = -1
    for i in range(len(data)):
        if data[i] == " ":
            arr.append(int(data[ind + 1:i]))
            ind = i

    # Формула для расчёта калорий для мужчин
    m = 88.36 + 13.4 * arr[0] + 4.8 * arr[1] - 5.7 * arr[2]

    # Формула для расчёта калорий для женщин
    w = 447.6 + 9.2 * arr[0] + 3.1 * arr[1] - 4.3 * arr[2]

    # Кнопки под сообщением
    InlKey = types.InlineKeyboardMarkup(row_width=2)
    man = types.InlineKeyboardButton("М", callback_data='male')
    woman = types.InlineKeyboardButton("Ж", callback_data='female')

    InlKey.add(man, woman)

    bot.send_message(message.chat.id, "Какой пол? - М/Ж", reply_markup=InlKey)

def router(message):
    """Функция возвращает пользователя из меню выбора продуктов"""
    vocabulary = {'Назад': welcome, 'Узнать каллорийность 👍' : product_name }
    vocabulary[message.text](message)

def product_name(message):
    """Функция отвечает за то, чтобы отправить пользователя к поиску любого продукта"""
    bot.send_message(message.chat.id, 'Введи продукт. Например, "Авокадо":')
    bot.register_next_step_handler(message, find)

def find(message):
    """Функция отвечает за поиск позиций в столбце "name" в базе данных в таблице "products".
    Возвращет данные в виде кнопок бота.
    """
    text = message.text
    cursor.execute("SELECT * FROM products WHERE name LIKE '%'||?||'%'", (text,))
    ans = cursor.fetchall()

    if len(ans) == 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("Узнать каллорийность 👍",)
        item2 = types.KeyboardButton("Назад")
        markup.add(item,item2)
        bot.send_message(message.chat.id, 'Таково у нас не водится, попробуй ещё раз', reply_markup=markup)
        bot.register_next_step_handler(message, router)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i, r in enumerate(ans):
            item = types.KeyboardButton(r[2])
            markup.add(item)
        bot.send_message(message.chat.id, "Что именно тебя интересует?", reply_markup=markup)
        bot.register_next_step_handler(message, output)

def output(message):
    """Функция отвечает за вывод данных(столбец "energy") позиций столбца "name" в базе данных в таблице "products"."""
    text = message.text
    cursor.execute("SELECT energy FROM products WHERE name=?", (text,))
    ans = cursor.fetchone()
    out = text + "\nНа 100 грамм: \n" + str(ans)[2:-3]
    bot.send_message(message.chat.id, out,reply_markup=None)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Узнать каллорийность 👍", )
    item2 = types.KeyboardButton("Назад")
    markup.add(item, item2)
    bot.send_message(message.chat.id, 'Что хотите сделать дальше?', reply_markup=markup)
    bot.register_next_step_handler(message, router)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    """Функция отвечает за кнопки, которые выводятся при выборе пола при расчёте калорий"""
    try:
        if call.message:
            if call.data == 'male':
                bot.send_message(call.message.chat.id, "Ваша норма калорий для мужчины составляет: " + str(m))
            elif call.data == 'female':
                bot.send_message(call.message.chat.id, "Ваша норма калорий для женщины составляет: " + str(w))

            # Убираем кнопки после выбора пользователя
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какой пол? - М/Ж",
                reply_markup=None)

    except Exception as e:
        print(repr(e))
# RUN
bot.polling(none_stop=True)