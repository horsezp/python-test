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