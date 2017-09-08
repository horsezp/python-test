#!/usr/bin/env python
# -*- coding:utf-8 -*-


import xlrd
import xlwt
import jieba
import chardet
import transferUtil

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

a=u'联系电话'
print a
print transferUtil.transfer(a)

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
        print ''
    else:
        v = v.strip()
    print "-----"+ v + "-------"
    list.append(v)
    s  = jieba.cut(v)
    print s
    for v1 in s:
        print v1
        v2= transferUtil.transfer(v1)
        print v2