#object类
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},今年{1}岁了'.format(self.name,self.age)

stu=Person('张三',20)
'''默认会调用__str__(self)这样的方法'''
print(stu)  #<__main__.Person object at 0x00000165EBA04BB0>    #我的名字是张三,今年20岁了
print(dir(stu))
print(type(stu))    #<class '__main__.Person'>


