import json
import socket

#6210407455
#6210406769

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

username = input("Username : ")

while True:

    request = {
            "user" : username,
            "protocal" : "XSS-DD",
        }

    request = bytes(json.dumps(request),encoding="utf-8")
    print(request)
    s.send(request)

    response = s.recv(1024)
    response = json.loads(response.decode('utf-8'))
    if response["status"] == "011 Success":
        print (response["status"])
        print (response["message"])
        break
    else :
        print (response["status"])
        print(response["message"])
        break