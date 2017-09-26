#encoding=gbk
import codecs

def isBlank (myString):
    return not (myString and myString.strip())

def isNotBlank (myString):
    return bool(myString and myString.strip())

map = {}
with codecs.open("D:/PycharmProjects/python-test/3.csv","r","gbk") as f:
    for line in f:
        #print(line)
        values =line.split(",")
        if isBlank(values[0]):
            continue
        print values[0]
        map[values[0]]=values[2]
f.close()

str = raw_input("请输入：");
print "你输入的内容是: ", str
codes =str.split("_")
for i in codes:
    print i
    print map[i]
