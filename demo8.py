#类中的特殊方法
a=20
b=100
c=a+b   #两个整数类型的对象的相加操作
d=a.__add__(b)  #底层操作
print(d)    #120
print(c)    #120

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):    #相加的话必须调用特殊方法
        return self.name+other.name
    def __len__(self):      #计算长度
        return len(self.name)

stu1=Student('张三')
stu2=Student('李四')
'''
s=stu1+stu2  #TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
print(s)'''
s=stu1.__add__(stu2)
print(s)    #张三李四
print('-----------------------')
lst=[11,22,33,44]
print(len(lst)) #4
print(lst.__len__())    #4

print(stu1.__len__())   #2
print(len(stu1))