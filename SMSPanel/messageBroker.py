import requests
import json
from config import *
from redis import Redis



client= Redis(REDIS_IP,REDIS_PORT)
phone_numbers = list()

def push_value(queue, value):
    try:
        client.lpop(queue)
        client.rpush(queue, value)
        return True
    except:
        return f'{value} does not push to {queue}'


def pop_value(queue):
        phone_numbers =client.blpop(queue)
        return phone_numbers

def send_sms(phone_number, message):
    url=f"http://ippanel.com/class/sms/webservice/send_url.php?from=+983000505&to={phone_number}&msg={message}&uname=FREE09196381290&pass=Faraz@0014589702"
    response =requests.get(url)
    print(response)
    # url = "https://api2.ippanel.com/api/v1/sms/pattern/normal/send"
    #
    # payload = json.dumps({
    #     "code": "your-pattern-code",
    #     "sender": "+983000505",
    #     "recipient": phone_number,
    #     "variable": {
    #         "verification-code": "test"
    #     },
    #
    #
    # })
    # headers = {
    #     'apikey': 'x_GJHLzs2h-s8dmURqX632dwWMC5YF0yO77Q2_YrWHw=',
    #     'Content-Type': 'application/json'
    # }
    #
    # response = requests.request("POST", url, headers=headers, data=payload)
    #
    # print(response.text)
