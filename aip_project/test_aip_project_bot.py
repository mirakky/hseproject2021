from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time

# Your API ID, hash and session string here
api_id = int('14422138')
api_hash = "22294f2929dd121b97a5f779a29ea514"
client = TelegramClient('@aloncess', api_id, api_hash)
client.start()


class TG_test(unittest.TestCase):
    def testStart(self):
        try:
            client.send_message('@calories_counter_bot', '/start')
            time.sleep(2)
            #messages = client.get_messages('@calories_counter_bot')
            for message in client.get_messages('@calories_counter_bot'):
                m = message.message
                #print(m)
            text = "Скажи, какую преследуешь цель?"
            self.assertEqual(m, text)
        except:
            self.assertFalse(True)