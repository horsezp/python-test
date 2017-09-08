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
db = conn.business_system  #����mydb���ݿ⣬û�����Զ�����
my_set = db.system_set #ʹ��test_set���ϣ�û�����Զ�����
my_set.remove()

file = 'D:/Users/ma.zipeng/Desktop/BI/2016��������Ϣϵͳ�嵥/��ֽ������Ϣϵͳ�嵥_2016.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016��������Ϣϵͳ�嵥/Խ�㷢չ-��Ϣϵͳ�����嵥2016.xlsx'
insertData(file,3,5)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016��������Ϣϵͳ�嵥/Խ��ز����_��Ϣϵͳ�嵥_201612.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016��������Ϣϵͳ�嵥/Խ�㽨��-��Ϣϵͳ�����嵥2016.xlsx'
insertData(file,4,5)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016��������Ϣϵͳ�嵥/Խ�㷿��-��Ϣϵͳ�嵥2016.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016��������Ϣϵͳ�嵥/Խ�㼯��_��ͨ���_��Ϣϵͳ�嵥_2016��ģ�棩-��ͨ.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016��������Ϣϵͳ�嵥/Խ�㼯��_�����ڻ�_��Ϣϵͳ�嵥_2016.xlsx'
insertData(file,2,3)

file = 'D:/Users/ma.zipeng/Desktop/BI/2016��������Ϣϵͳ�嵥/Խ�㼯��_��ذ��_��Ϣϵͳ�嵥_2016.xlsx'
insertData(file,2,3)

for i in my_set.find():
    print(i)