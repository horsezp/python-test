#!/usr/bin/python
#coding=utf-8
import requests
import cx_Oracle

def getQuote(code):
    r = requests.get("http://hq.sinajs.cn/list="+code)
    # 爬取新浪股票 API
    res = r.text.split(',')
    print res
    return res

value = getQuote("hk00405")
print "price" + value[2]

value = getQuote("hk87001")
print "price" + value[2]

value = getQuote("hk01426")
print "price" + value[2]

value = getQuote("hk01275")
print "price" + value[2]

value = getQuote("hk06139")
print "price" + value[2]


#db=cx_Oracle.connect('system','oracle','192.168.2.42:1521/dave')

#print db.version

#db.close()