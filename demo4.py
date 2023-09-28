#继承
#方法重写
class Preson(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Preson):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id=id
    def info(self):
        super().info()
        print('学号',self.id)
class Teacher(Preson):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age,)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print('教龄',self.teachofyear)

stu=Student('张三',30,111)
tea=Teacher('李四',90,50)
stu.info()  #张三 30
            #学号 111
print('---------------------------')
tea.info()  #李四 90
            #教龄 50
            