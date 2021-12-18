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
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Скажи, какую преследуешь цель?"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_4(self):
        try:
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Скажи, какую преследуешь цель?"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_5(self):
        try:
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Скажи, какую преследуешь цель?"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_6(self):
        try:
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Скажи, какую преследуешь цель?"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)
    def test_7(self):
        try:
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
            text = "Скажи, какую преследуешь цель?"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)