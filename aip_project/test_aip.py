from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time


#Данные пользователя, необходимо зайти на официальный сайт https://my.telegram.org/
api_id = 14422138
api_hash = "22294f2929dd121b97a5f779a29ea514"
client = TelegramClient('@aloncess', api_id, api_hash)


client.start()


class testBotCommmands(unittest.TestCase):
    def test_1(self):
        try:
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = "Скажи, какую преследуешь цель?"
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_2(self):
        try:
            client.send_message('@calories_counter_bot', 'Узнать норму калорий 🍔')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = "Укажите ваши параметры Вес, Рост и Возраст в формате: \n'Веc Рост Возраст'"
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_3(self):
        try:
            client.send_message('@calories_counter_bot', '100 100 100')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = "Какой пол? - М/Ж"
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def test_4(self):
        try:
            client.send_message('@calories_counter_bot', 'Ж')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = "Скажи, какую преследуешь цель?"
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_5(self):
        try:
            client.send_message('@calories_counter_bot', 'Узнать каллорийность 👍')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = '"Введи продукт. Например, "Авокадо":"'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)


    def test_6(self):
        try:
            client.send_message('@calories_counter_bot', 'Ролл')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = "Что именно тебя интересует?"
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_7(self):
        try:
            client.send_message('@calories_counter_bot', 'Ролл «Симфония» с креветкой')
            time.sleep(2)
            messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = "Ролл «Симфония» с креветкой\nНа 100 грамм: \nбелки 6,5 г;  жиры 10,1 г;  углеводы 17,2 г;  185,7 ккал;"
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)


