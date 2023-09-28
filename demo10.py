#类的赋值与浅拷贝与深拷贝
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#(1)类对象的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
'''
<__main__.CPU object at 0x000002B9457102B0> 2994757239472
<__main__.CPU object at 0x000002B9457102B0> 2994757239472
'''
#类的浅拷贝:拷贝时，对象包含的子对象不拷贝，源对象与拷贝对象会引用同一个子对象
print('------------------------------------------------------')
disk=Disk() #创建一个硬盘类的对象
computer=Computer(cpu1,disk) #创建一个计算机类的对象
print(disk) #<__main__.Disk object at 0x0000025174EED6D0>
#浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
'''
<__main__.Computer object at 0x000002B9DD72D820> <__main__.CPU object at 0x000002B9DD72D7C0> 
<__main__.Disk object at 0x000002B9DD72D6D0>
'''
print(computer2,computer2.cpu,computer2.disk)
'''
<__main__.Computer object at 0x000002B9DD6F0F40> <__main__.CPU object at 0x000002B9DD72D7C0> 
<__main__.Disk object at 0x000002B9DD72D6D0>
'''
#深拷贝
print('****************************************')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
'''
****************************************
<__main__.Computer object at 0x0000021A0E4FD820> <__main__.CPU object at 0x0000021A0E4FD7C0>
 <__main__.Disk object at 0x0000021A0E4FD6D0>
<__main__.Computer object at 0x0000021A0E4FE4F0> <__main__.CPU object at 0x0000021A0E570310>
 <__main__.Disk object at 0x0000021A0E570340>
'''