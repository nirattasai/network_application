import socket
from datetime import date
from random import randint
import json
from typing import ContextManager

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

s.listen(5)

today = date.today()
lucky_number = randint(0,99)
user = ['nirattasai','issaraphap']


while True:
    clientsocket, address = s.accept()
    request = clientsocket.recv(1024)
    data = json.loads(request.decode("utf-8"))
    print(address)

    if data["protocal"] != "XSS-DD":
        response = {
            "status" : "099 Wrong_Protocal",
            "message" : "Wrong Protocalng"
        }

    elif data["user"] in user:
        print(data["user"])
        response = {
            "protocal" : "XSS-DD",
            "status" : "011 Success",
            "message" : "today is : "+str(today)+"\n"+"weather is : sunny \nlucky number :"+str(lucky_number)
        }
    else :
        response = {
            "protocal" : "XSS-DD",
            "status" : "022 Denied",
            "message" : "You are not member"
        }

    response = bytes(json.dumps(response),encoding="utf-8")
    print(response)
    clientsocket.send(response)