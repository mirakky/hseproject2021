from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time

#@calories_counter_bot
#TOKEN = '2083515169:AAHMzCHTajIgUM4va0jFtaFSayaOUBu7b6k'

api_id = int("")
api_hash = "2083515169:AAHMzCHTajIgUM4va0jFtaFSayaOUBu7b6k"
session_str = "TELETHON_SESSION"
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your session string is:", client.session.save())

client = TelegramClient(session_str, api_id, api_hash)

client.start()

class AipProjectTest(unittest.TestCase):
    def testWelcome(self):
        try:
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'fathutnik, добро пожаловать в MIEMUniversalBot 🤩 \n\nДанный бот имеет множество различных полезных команд, все они приведены в списке ниже! \n\n/convert - команда для конвертации валюты!\n/get_coffee_picture - команда для получения рандомной картинки кофе!\n/update_math_skills - команда для прокачки большого ума!\n/get_smart_quote - команда для получения пищи для размышлений!\n\/shakal_picture - команда для шакалинга картинки!'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testFuncs(self):
        try:
            client.send_message('@calories_counter_bot', 'Хочу кофе')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Вот ваша фоточка прекрасного напитка'
            self.assertRegex(m, text)
            client.send_message('@calories_counter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testGet_Parms(self):
        try:
            time.sleep(2)
            client.send_message('@calories_counter_bot', 'Хочу поумничать перед друзьями')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Как однажды сказал'
            self.assertRegex(m, text)
            client.send_message('@calories_counter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testRouter(self):
        try:
            time.sleep(2)
            client.send_message('@calories_counter_bot', 'Надо чето с картинкой подшаманить ')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Отправьте картинку, которую надо зашакалить Ꮗ'
            self.assertRegex(m, text)
            client.send_message('@calories_counter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testProduct_Name(self):
        try:
            time.sleep(2)
            client.send_message('@calories_counter_bot', 'Надо к матану готовиться')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Вам предлагается решить данный пример для увеличения своей скорости счета, чем быстрее решите, тем лучше!'
            self.assertRegex(m, text)
            client.send_message('@calories_counter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testFind(self):
        try:
            time.sleep(2)
            client.send_message('@calories_counter_bot', 'Мне бы валюту конвертировать 💶')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'fathutnik, выберите интересующую вас валютную пару для перевода или впишите свою 🤩'
            self.assertRegex(m, text)
            client.send_message('@calories_counter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testOutput(self):
        try:
            time.sleep(2)
            client.send_message('@calories_counter_bot', 'Мне бы валюту конвертировать 💶')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'fathutnik, выберите интересующую вас валютную пару для перевода или впишите свою 🤩'
            self.assertRegex(m, text)
            client.send_message('@calories_counter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testCallback_inline(self):
        try:
            time.sleep(2)
            client.send_message('@calories_counter_bot', 'Мне бы валюту конвертировать 💶')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'fathutnik, выберите интересующую вас валютную пару для перевода или впишите свою 🤩'
            self.assertRegex(m, text)
            client.send_message('@calories_counter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)