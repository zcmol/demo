import itchat
from itchat.content import *
import requests
import json

ROBOT_URL = 'http://openapi.tuling123.com/openapi/api/v2'
ROBOT_API_KEY = '9992d22924e64c68a27447b92e378e70'
ROBOT_SECRET_KEY = '4b78d1326fda6770'

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg)
    itchat.send_msg('123345', toUserName=msg.User.RemarkName)
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {"text": msg.text}
        },
        "userInfo": {
            "apiKey": ROBOT_API_KEY,
            "userId": '123456'
        }
        
    }
#    call_tu_ling(json.dumps(data));

# 访问图灵
def call_tu_ling(data):
    res = requests.post(ROBOT_URL, data=data)
    print(res.text)

itchat.auto_login()
itchat.run()
