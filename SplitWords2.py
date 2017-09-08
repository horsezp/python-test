#!/usr/bin/env python
# -*- coding:gbk -*-

from snownlp import SnowNLP
import xlrd
import xlwt
from textblob import TextBlob


file = 'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/广纸集团信息系统清单_2016.xlsx'
data = xlrd.open_workbook(file)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
list = []
for i in range(ncols):
    v = table.cell(2, i).value
    v = v.replace("\n", " ")
    print "-----"+ v + "-------"
    list.append(v)
    s = SnowNLP(v)
    print s.words
    for v in s.words:
        print v