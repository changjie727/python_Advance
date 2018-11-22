__author__ = 'changjie'

import math

def add(x,y,f):
    if x > y:
        return f(x)+f(y)
    else:
        return f(y)+f(x)

print add(25,9,math.sqrt)
