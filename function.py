#!/usr/bin/python
#coding=utf-8
# 可写函数说明
def printme( str ):
    "打印任何传入的字符串"
    print str;
    return;


# 调用printme函数
printme( str = "My string");


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;


# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)

# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);