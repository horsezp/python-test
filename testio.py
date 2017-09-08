#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
#str = raw_input("请输入：");
#print "你输入的内容是: ", str

try:
    f = open('D:/Users/ma.zipeng/Desktop/delete data.sql1', 'r')
    for line in f:
        print(line)
        params =line.split(' ')
        for p in params:
            print p
except Exception,Argument: #
    print "Error: 没有找到文件或读取文件失败",Argument
else:
    if f:
        f.close()
result = list()
with codecs.open("D:/Users/ma.zipeng/Desktop/delete data.sql","r","utf-8") as f:
    for line in f:
        print(line)
        result.append(line)
print result
f.close()
open('result-readline.txt', 'w').write('%s' % '\n'.join(result))
