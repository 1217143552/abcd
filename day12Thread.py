# from threading import Thread
# import time
#
# basket = 0#篮子
# amount = 0#总销售额
#
#
# class Cooker(Thread):
#     name=""
#     num = 0
#     def run(self) -> None:
#         global basket
#         while True:
#             if basket!=500:
#                 self.num +=1
#                 basket+=1
#             else:
#                 time.sleep(3)
#                 continue
#         print(self.name,self.num)
#         print("应支付给%s工资%s元"%(self.name,2.5*self.num))
#
#  class Customer(Thread):
#     money=5000
#     def run(self) -> None:
#         while True:
#             global basket
#             if basket==0:
#                 time.sleep(4)
#             else:
#                 basket-=1
#                 self.money-=3
#                 if self.money<3:
#                     break
#
# cooker1=Cooker()
# cooker2=Cooker()
# cooker3=Cooker()
#
# cus1=Customer()
# cus2=Customer()
# cus3=Customer()
# cus4=Customer()
# cus5=Customer()
# cus6=Customer()
#
# cooker1.name="张三"
# cooker2.name="李四"
# cooker3.name="王五"
#
# cooker1.start()
# cooker2.start()
# cooker3.start()
# cus1.start()
# cus2.start()
# cus3.start()
# cus4.start()
# cus5.start()
# cus6.start()

from threading import Thread
import time

basket = 0#篮子
amount = 0#总销售额

#厨师类
class Cooker(Thread):
    cookername=""
    num=0
    def run(self) -> None:
        global basket
        while True:
            if basket<500:
                self.num = self.num + 1
                basket += 1
                print(self.name, "做了", self.num, "个蛋糕")
            else:
                time.sleep(3)
                continue
        print(self.name,"的工资为",2.5*self.num)

class Customer(Thread):
    money=5000
    def run(self) -> None:
        while True:
            global basket
            if basket==0:
                time.sleep(4)
            else:
                basket-=1
                self.money-=3
                if self.money<3:
                    break

cooker1=Cooker()
cooker2=Cooker()
cooker3=Cooker()

cus1=Customer()
cus2=Customer()
cus3=Customer()
cus4=Customer()
cus5=Customer()
cus6=Customer()

cooker1.name="张三"
cooker2.name="李四"
cooker3.name="王五"

cooker1.start()
cooker2.start()
cooker3.start()
cus1.start()
cus2.start()
cus3.start()
cus4.start()
cus5.start()
cus6.start()