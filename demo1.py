#面向对象的三大特征
#封装#继承#多态
'''封装：提高程序的安全性'''
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已经启动')

car=Car('宝马X5')
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在外部被使用，前面加__
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()  #张三 20
print(stu.name) #张三
'''在类的外部使用name和age'''
print(dir(stu))
'''['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 'name', 'show']'''
print(stu._Student__age)    #20#可以通过_Student__age，访问