import json
import random
import os
import sys
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def hello(event, context):
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["chat"]["first_name"]

        response = "Please /start, {}".format(first_name)

        if "start" in message:
            response = "Hola {}".format(first_name)
        if "end" in message:
            response = "Adieu {}".format(first_name)

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = BASE_URL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}

def daily(event, context):

    myGroupChatId = -1001694547978
    myMessages = [
    "Hola , como estas?",
    "Hola , como amaneciste?",
    "Hola , como estas?",
    "Hola , como amaneciste?",
    "Hola , te amo tanto",
    "Hola , ten bonito dia"
    ]
    response =  random.choice(myMessages)
    try:
        data = {"text": response.encode("utf8"), "chat_id": myGroupChatId}
        url = BASE_URL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}