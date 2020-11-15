import requests
import logging
from config import ADMIN
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "1460584540:AAFbo8lS_tfXzoMfgWY0BtiueqimNojcq2M"
ADMIN_ID = "224483345"


class NotificationManager:

    def __init__(self, BOT_TOKEN, ADMIN_ID):
        self.token = BOT_TOKEN
        self.chat_id = ADMIN_ID

    def send_sms(self, message='bla-bla-bla'):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        payload = {'chat_id': self.chat_id, 'text': message}
        r = requests.post(url, json = payload)
        return r

