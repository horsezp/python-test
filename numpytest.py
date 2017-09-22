#!/usr/bin/python
#coding=utf-8
import numpy as np

def MaxMinNormalization(x,Max,Min):
    x = round((float)(x - Min) / (float)(Max - Min),2);
    return x;

def Z_ScoreNormalization(x,mu,sigma):
    x = (x - mu) / sigma;
    return x;

def sigmoid(X,useStatus):
    if useStatus:
        return 1.0 / (1 + np.exp(-float(X)));
    else:
        return float(X);

print np.array([1,2,3,4])
v = np.array([1,2,3,4])

min=v.min()
max=v.max()

mu=np.average(v)
sigma=v.std()


print map(lambda x: MaxMinNormalization(x,max,min),v)

print map(lambda x: Z_ScoreNormalization(x,mu,sigma),v)

print map(lambda x: sigmoid(x,True),v)