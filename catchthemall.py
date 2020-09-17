#!/usr/bin/python3
# -*- coding: utf-8 -*-
import base64


o = b''
with open("catchthemall.txt", "r") as f: 
    count = 0
    for line in f:
        if (count + 1) % 8 == 0:
            l = base64.b64decode(line)
            print(l)
        count += 1


            
