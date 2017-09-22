#!/usr/bin/python
#coding=utf-8

import tushare as ts

df = ts.get_realtime_quotes('000405') #Single stock symbol
v= df[['code','name','price','bid','ask','volume','amount','time']]
print v


