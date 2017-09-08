#!/usr/bin/env python
# -*- coding:gbk -*-

from pymongo import MongoClient
import xlrd
import xlwt
import os

def insertData(file, headLine , startLine):
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols

    print nrows
    print ncols

    list =[]
    for i in range(ncols ):
        v= table.cell(headLine,i).value
        v = v.replace("\n"," ")
        print v
        list.append(v)

    for i in range(startLine,nrows):
        #print i
        dist={}
        if not table.cell(i,1).value.strip():
            continue
        for j in range(ncols):
            v= table.cell(i,j).value
            print v
            dist[list[j]] =v
        print dist
        my_set.insert(dist)

conn = MongoClient('127.0.0.1', 27017)
db = conn.business_system  #连接mydb数据库，没有则自动创建
my_set = db.system_set #使用test_set集合，没有则自动创建
my_set.remove()

file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/广纸集团信息系统清单_2016.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/越秀发展-信息系统更新清单2016.xlsx'
insertData(file,3,5)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/越秀地产板块_信息系统清单_201612.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/越秀建材-信息系统更新清单2016.xlsx'
insertData(file,4,5)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/越秀房托-信息系统清单2016.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/越秀集团_交通板块_信息系统清单_2016（模版）-交通.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/越秀集团_广州期货_信息系统清单_2016.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/越秀集团_金控板块_信息系统清单_2016.xlsx'
insertData(file,2,3)

for i in my_set.find():
    print(i)