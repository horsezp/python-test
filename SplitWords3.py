#!/usr/bin/env python
# -*- coding:utf-8 -*-


import xlrd
import xlwt
import jieba
import chardet

w ="-----首次投入费用 （万元）-------"
print chardet.detect(w)
nPos = w.find("（")
print nPos
w = w[0:nPos]
print w

file = u'D:/Users/ma.zipeng/Desktop/BI/2016年各板块信息系统清单/广纸集团信息系统清单_2016.xlsx'
data = xlrd.open_workbook(file)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
list = []
for i in range(ncols):
    v = table.cell(2, i).value
    v = v.replace("\n", " ")
    try:
      nPos = v.index(" ")
      v = v[0:nPos]
    except  ValueError:
        print 'error'
    else:
        v = v.strip()
    print "-----"+ v + "-------"
    list.append(v)
    s =seg_list = jieba.cut(v)
    print s
    for v in s:
        print v