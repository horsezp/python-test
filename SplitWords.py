#!/usr/bin/env python
# -*- coding:gbk -*-

from snownlp import SnowNLP

from textblob import TextBlob

s = SnowNLP(u'这个东西真心很赞')

print s.words
for v in s.words:
    print v