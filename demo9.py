#特殊方法
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用了，cls的值为{0}'.format(id(cls)))  #2271101801280
        obj=super().__new__(cls)
        print('创建的对象id为：{0}'.format(id(obj)))   #2271100785280
        return obj  #返回给self

    def __init__(self,name,age):    #self给了p1
        print('__init__被调用了，self的id值为{0}'.format(id(self))) #2271100785280
        self.name=name
        self.age=age

print('object这个类对象的id为：{0}'.format(id(object))) #2271100785280
print('Person这个类对象的id为：{0}'.format(id(Person))) #2271100785280

#创建Person类的实例对象
p1=Person('张三',20)  # = 赋值，先执行右侧代码
print('p1这个Person类的实例对象的id为:{0}'.format(id(p1)))    #2271100785280

'''object这个类对象的id为：140718542872064
Person这个类对象的id为：2271101801280
__new__被调用了，cls的值为2271101801280
创建的对象id为：2271100785280
__init__被调用了，self的id值为2271100785280
p1这个Person类的实例对象的id为:2271100785280'''

