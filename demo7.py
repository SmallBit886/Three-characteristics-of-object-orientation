#类当中的特殊属性
#print(dir(object))

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#创建C的类对象
x=C('Jack',20)  #x是C类型的一个实例对象
print(x.__dict__)   #实例对象的属性字典
'''{'name': 'Jack', 'age': 20}'''
print(C.__dict__)   #类对象的属性方法
'''{'__module__': '__main__', '__init__': <function C.__init__ at 0x00000270D12A0820>, '__doc__': None}'''
print('-----------------------------------------------------------------------------------------------------')
print(x.__class__)  #<class '__main__.C'>   #输出了对象所属的类
print(C.__bases__)  #(<class '__main__.A'>, <class '__main__.B'>)   #输出的C类父类类型的元组
print(C.__base__)   #<class '__main__.A'>   #输出前面的父类，类的基类
print(C.__mro__)    #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)   #类的层次结构
print(A.__subclasses__())   #[<class '__main__.C'>] #查看A的子类 的列表
