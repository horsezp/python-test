#!/usr/bin/env python
# -*- coding:gbk -*-

from snownlp import SnowNLP

from textblob import TextBlob

s = SnowNLP(u'����������ĺ���')

print s.words
for v in s.words:
    print v