__author__ = 'changjie'

import math

def is_sqr(x):
    a=math.sqrt(x)
    return a==int(a)

print filter(is_sqr,range(1,101))
