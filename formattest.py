#!/usr/bin/python
#coding=utf-8

print "the value is %8.3f" % 3.14140021

print "%-8.3f" % 10. + "\n" + "%-8.3f" % -100.

print "I am %i years old and %.3f meters tall." % (30, 1.83)

s = "There are 5 cars."
s = s[:10] + "6" + s[11:]
print s