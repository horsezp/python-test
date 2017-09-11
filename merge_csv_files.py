#encoding=utf-8
import codecs

def isBlank (myString):
    return not (myString and myString.strip())

def isNotBlank (myString):
    return bool(myString and myString.strip())

result = list()
map = {}
with codecs.open("D:/Users/ma.zipeng/Desktop/BI/namestandard/1.csv","r","gbk") as f:
    for line in f:
        #print(line)
        values =line.split(",")
        if isBlank(values[0]):
            continue
        #print values[0]
        map[values[0]]=line
        result.append(line)
print len(result)
f.close()

print len(map)

with codecs.open("D:/Users/ma.zipeng/Desktop/BI/namestandard/2.csv","r","gbk") as f:
    for line in f:
        #print(line)
        values =line.split(",")
        if isBlank(values[0]):
            continue
        #print values[0]
        map[values[0]]=line
        result.append(line)
print len(result)
f.close()

print len(map)


fo=codecs.open("D:/Users/ma.zipeng/Desktop/BI/namestandard/3.csv","w","gbk")
for line in [ v for v in sorted(map.values())]:
    #print line
    fo.writelines(line)
fo.close()