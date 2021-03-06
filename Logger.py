import requests
from logging import Handler, Formatter
import logging
import datetime

TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = ''

class RequestsHandler(Handler):
    def emit(self, record):
        log_entry = self.format(record)
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': log_entry,
            'parse_mode': 'HTML'
        }
        return requests.post("https://api.telegram.org/bot{token}/sendMessage".format(token=TELEGRAM_TOKEN),
                             data=payload).content

class LogstashFormatter(Formatter):
    def __init__(self):
        super(LogstashFormatter, self).__init__()

    def format(self, record):
        t = datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')

        return "<i>{datetime}</i><pre>\n{message}</pre>".format(message=record.msg, datetime=t)


def getLogger():
    logger = logging.getLogger('telegram-notfier')
    logger.setLevel(logging.WARNING)
    handler = RequestsHandler()
    formatter = LogstashFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)

    return logger