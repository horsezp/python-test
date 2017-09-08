#!/usr/bin/python
#coding=utf-8
import xdrlib, sys
import xlrd
import xlwt
data = xlrd.open_workbook('D:/Users/ma.zipeng/Desktop/BI/mapping.xlsx')

table = data.sheets()[0]

nrows = table.nrows
print nrows
for i in range(nrows ):
    print table.cell(i,0).value
    print table.cell(i, 1).value

