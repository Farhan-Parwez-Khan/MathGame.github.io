# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:18:18 2024

@author: FARHAN PARWEZ KHAN
"""
import random
import time
f=time.time()
while 1:
    a=random.randint(0, 10)
    b=random.randint(0, 10)
    c=random.choice('+' '-' 'x' '/')
    if c=='/':
        a=random.randint(1, 10)*b
    print(a,c,b)
    y=int(input('Enter Your Answer:'))
    if c=='+' and y==(a+b):
        print('correct')
    elif c=='-' and y==(a-b):
        print('correct')
    elif c=='x' and y==(a*b):
        print('correct')
    elif c=='/' and y==(a/b):
        print('correct')
    else:
        print('wrong')
        break
    if time.time()-f>=10:
        print("Time's up" )
        break
