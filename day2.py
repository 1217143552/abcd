"""
猜数字游戏，有5个金币，猜错一次金币减一，才对一次金币加2，有三次猜测机会，金币为0则停止猜数
"""
import random
randint=random.randint(10,20)
print(randint)
print("\n")

i=1
cash = 5
while i<=10:
    num = int(input("请输入在10-20范围间的整数："))
    print("\n")
    if num==randint:
        print("猜对了")
        cash=cash+3
        break
    elif num<randint:
        print("猜小了")
        cash=cash-1
        i+=1
    else:
        print("猜大了")
        cash = cash-1
        i+=1
    if cash==0:
        print("没有金币了，充钱吧")
        print("输入充钱数")
        a=int(input())
        cash=cash+a
    if i==10:
        print("次数用光了")
        break