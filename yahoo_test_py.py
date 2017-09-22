#!/usr/bin/python
#coding=utf-8
from yahoo_finance import Share
yahoo = Share('0405.HK')
print yahoo.get_open()
print yahoo.get_price()
print yahoo.get_prev_close();
print yahoo.get_trade_datetime()

#87001.HK  1426.HK  1275.HK 6139.HK

yahoo = Share('87001.HK')
print yahoo.get_open()
print yahoo.get_price()
print yahoo.get_trade_datetime()

