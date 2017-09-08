#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


class Employee:
    '所有员工的基类 like java class static fields share by all class instance and class'
    empCount = 0

    #this is specify method name for initial
    def __init__(self, name, salary):
        #here define the instance level property
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    #self like this , it need in the method param but does not need to pass in when invoke
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp1.displayCount();
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


print hasattr(emp1, 'name')    # 如果存在 'age' 属性返回 True。
print getattr(emp1, 'name')    # 返回 'age' 属性的值
print setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
print getattr(emp1, 'age')    # 返回 'age' 属性的值
print delattr(emp1, 'age')    # 删除属性 'age'
print hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__