#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket

host = '127.0.0.1'
port = 19999

r=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((host, port))

x=0

while(x<7):
        d=r.recv(2048).decode()
        print(d)

            
        s=d.split("'")[-2]
        print(s)
        c = chr(int(s,2))
        print(c)
        r.send((c+'\n').encode())
        x=x+1
