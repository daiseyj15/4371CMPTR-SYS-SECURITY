#!/usr/bin/python3
#-*-coding: utf-8 -*-
import base64, socket

host = '127.0.0.1'
port = 11111

r=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((host,port))

x=0

while(x<10002):
        d=r.recv(2048).decode()
        print(d)
        #if "==" not in d:
        #    break
        s= base64.b64decode(d).decode()
        print(s)
        r.send((s+'\n').encode())
        x=x+1
