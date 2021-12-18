from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time

# Your API ID, hash and session string here
api_id = int('')
api_hash = ""
client = TelegramClient('', api_id, api_hash)
client.start()


class TG_test(unittest.TestCase):
    def testStart(self):
        try:
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Скажи, какую преследуешь цель?"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_2(self):
        try:
            client.send_message('@calories_counter_bot', 'Узнать каллорийность 👍')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = '"Введи продукт. Например, "Авокадо":"'
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_3(self):
        try:
            client.send_message('@calories_counter_bot', 'Узнать норму калорий 🍔')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Укажите ваши параметры Вес, Рост и Возраст в формате: \n'Веc Рост Возраст'"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_4(self):
        try:
            client.send_message('@calories_counter_bot', '100 100 100')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Какой пол? - М/Ж"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_5(self):
        try:
            client.send_message('@calories_counter_bot', 'Ж')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Ваша норма калорий для женщины составляет: 1247.6"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_6(self):
        try:
            client.send_message('@calories_counter_bot', 'Ролл')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Что именно тебя интересует?"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_7(self):
        try:
            client.send_message('@calories_counter_bot', 'Ролл «Симфония» с креветкой')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Ролл «Симфония» с креветкой\nНа 100 грамм: \nбелки 6,5 г;  жиры 10,1 г;  углеводы 17,2 г;  185,7 ккал;"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)