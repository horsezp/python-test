#!/usr/bin/python
#coding=utf-8
from functools import reduce
def MaxMinNormalization(x,Max,Min):
    x = round((float)(x - Min) / (float)(Max - Min),2);
    return x;

print MaxMinNormalization(12,100,1)

print map( lambda x : x + 1, [1, 2, 3] )

l = [1,2,3,4,5-9,0,45,-99]
print map(lambda x: abs(x),l)

print filter(lambda x: x<0 ,l)

print reduce(lambda x,y: x+y,l)

