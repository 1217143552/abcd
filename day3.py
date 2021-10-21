"""
随机点名然后处罚遍数
#优化代码：只有一个input 进行判断 1or2 生成人名or几遍    q or Q退出  输入其他的直接锁死time.sleep(10)睡10秒
"""

import random
import time

name=["嬴政","刘邦","项羽","曹操","刘备", "孙策","武则天","司马懿","刘禅","成吉思汗"]

dint=random.randint(0,len(name)-1)
print(name[dint])
