#多态
#Python动态语言
class Animal:
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头。。。')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼。。。')

class Persion:
    def eat(self):
        print('人吃五谷杂粮。。。')

#定义一个函数
def fun(ojb):
    ojb.eat()

fun(Dog())
fun(Cat())
fun(Animal())   #动物会吃
'''--------------不存在继承关系，但是有eat（）方法-------------'''
fun(Persion())
'''
狗吃骨头。。。
猫吃鱼。。。
人吃五谷杂粮。。。
'''
