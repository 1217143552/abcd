from DBUtils import update
from DBUtils import select
import random
class welcome:
    def welcome(self):
        print("***************************")
        print("*    中国工商银行          *")
        print("*     账户管理系统         *")
        print("***************************")
        print(" ")
        print("*1、开户                   *")
        print("*2、存钱                   *")
        print("*3、取钱                   *")
        print("*4、转账                   *")
        print("*5、查询                   *")
        print("*6、欢迎下次光临            *")
        print("****************************")
wel=welcome()
wel.welcome()
#初始化银行
bank={}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="工商银行"

class gongshang:
    def useradd(self):
        account=random.randint(10000000,99999999)
        name=input("请输入您的名称")
        password=int(input("请输入您的密码"))
        print("请输入你的详细信息")
        country=input("\t\t请输入您的国籍")#\t ==tab
        province=input("\t\t请输入您的省份")
        steert=input("\t\t请输入您的街道")
        door=input("\t\t请输入您的门牌号")
        money=0
        num=self.bankadd(account,name,password,country,province,steert,door,money)
        if num ==3:
            print("本银行已满请到其他银行开户")
        elif num== 2:
            print("用户已存在")
        elif num==1:
            print("恭喜你开户成功，以下是您的相信信息")
            sql3 = "select account 账号,name 姓名,password 密码,country 国家,province 省份,steert 街道,door 门牌号,money 货币,bankename 银行名称 from gongshang where name = %s "
            param3 = [name]
            data3 = select(sql3, param3)
            print("账号:",account
              ,"姓名:",name
              ,"密码:",password
              ,"国家:",country
              ,"省份:",province
              ,"街道:",steert
              ,"门牌号:",door
              ,"货币:",money
              ,"银行名称:",bank_name
              )
    def bankadd(self,account,name,password,country,province,steert,door,money):
        sql = "select count(*) from gongshang"
        param = []
        data = select(sql,param,mode="one")
        if data[0] >= 100:
            return 3


        sql1 = "select * from gongshang where name = %s"
        param1 = [name]
        data1 = select(sql1, param1)  # ((),)
        if len(data1) >= 1:
            return 2

        sql2 = "insert into gongshang value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [account,name,password,country, province, steert, door, money, bank_name]
        update(sql2, param2)
        return 1

    def cunqianadd(self):
        name=input("请输入您的姓名：")

        num1=self.cqadd(name)


        if num1==False:
            print("银行没有该用户信息")
        elif num1==True:
            sql3 = "select * from gongshang where name = %s "
            param3 = [name]
            data3 = select(sql3, param3)
            for i in data3:
                print(i)
    def cqadd(self,name):
        sql1 = "select * from gongshang where name = %s"
        param1 = [name]
        data1 = select(sql1, param1)  # ((),)
        if len(data1) >= 1:
            sql2 = "update gongshang set money=money+%s where name=%s "
            song=int(input("请输入您要存入的金额："))
            param2 = [song,name]
            update(sql2, param2)
            return True
        else:
            return False

    def quxianadd(self):
        name = input("请输入您的姓名：")
        password = int(input("请输入您的用户密码："))
        num2 = self.qxadd(name,password)

        if num2==1:
            print("账户信息不存在")
        elif num2==2:
            print("密码输入错误")
        elif num2==3:
            print("您的余额不足")
        elif num2==0:
            sql3 = "select * from gongshang where name = %s "
            param3 = [name]
            data3 = select(sql3, param3)
            for i in data3:
                print(i)
    def qxadd(self,name,password):
        sql3 = "select * from gongshang where name = %s and password=%s"
        param3 = [name,password]
        data3 = select(sql3, param3)  # ((),)
        if len(data3) >= 1:
            sql4="select money from gongshang where name = %s"
            param4=[name]
            data4=select(sql4,param4)
            for i in data4:
                print(i)

            song1=int(input("请输入您要取出的金额："))

            sql1="select money from gongshang where money>%s"
            param1=[song1]
            data1=select(sql1,param1)
            if len(data1)==0:
                return 3
            elif len(data1)>=1:
                sql5 = "update gongshang set money=money-%s where name = %s"
                param5 = [song1,name]
                update(sql5, param5)
                return 0
        sql6 = "select * from gongshang where name = %s "
        param6 = [name]
        data6 = select(sql6, param6)  # ((),)
        if len(data6)==0:
            return 1
        sql7 = "select * from gongshang where password = %s "
        param7 = [password]
        data7 = select(sql7, param7)  # ((),)
        if len(data7) == 0:
            return  2

    def zhuanzhangadd(self):
        zhuanchuname=input("请输入您转出账户的姓名：")
        zhuanruname=input("请输入您转入账户的姓名：")
        password = int(input("请输入您的用户密码："))
        num3=self.zzadd(zhuanchuname,zhuanruname,password)

        if num3==1:
            print("转出或转入的账号不存在")
        elif num3==2:
            print("转出账户的密码输入错误")
        elif num3==3:
            print("转出账户的余额不足")
        elif num3==0:
            sql3 = "select * from gongshang where name = %s "
            param3 = [zhuanchuname]
            data3 = select(sql3, param3)
            for i in data3:
                print(i)
            sql2 = "select * from gongshang where name = %s "
            param2= [zhuanruname]
            data2 = select(sql2, param2)
            for i in data2:
                print(i)
    def zzadd(self,zhuanchuname,zhuanruname,password):
        sql3 = "select * from gongshang where name = %s "
        param3 = [zhuanchuname]
        data3 = select(sql3, param3)
        sql1 = "select * from gongshang where name = %s "
        param1 = [zhuanruname]
        data1 = select(sql1, param1)
        sql2 = "select * from gongshang where password = %s "
        param2 = [password]
        data2 = select(sql2, param2)
        if len(data3) >= 1 and len(data1) >= 1:
            if len(data2) >= 1:
                zhuanrumoney = int(input("请输入您要转出的金额："))
                sql7 = "select * from gongshang where money>%s "
                param7 = [zhuanrumoney]
                data7 = select(sql7, param7)
                if len(data7) < 0:
                    return 3
                elif len(data7) >= 1:
                    sql4 = "update gongshang  set money=money+%s where name=%s "
                    param4 = [zhuanrumoney, zhuanruname]
                    update(sql4, param4)
                    sql5 = "update gongshang set money=money-%s where name=%s "
                    param5 = [zhuanrumoney, zhuanchuname]
                    update(sql5, param5)
                    return 0
        if len(data3) < 1 or len(data1) < 1:
            return 1
        if len(data2) < 1:
            return 2

    def chaxunadd(self):
        name = input("请输入您的姓名：")
        password = int(input("请输入您的用户密码："))
        num4 = self.cxadd(name, password)

        if num4==1:
            print("账户信息不存在")
        elif num4==2:
            print("密码输入错误")
        elif num4==0:
            sql3 = "select * from gongshang where name = %s "
            param3 = [name]
            data3 = select(sql3, param3)
            for i in data3:
                print( i )
    def cxadd(self,name,password):
        sql3 = "select * from gongshang where name = %s "
        param3 = [name]
        data3 = select(sql3, param3)
        sql2 = "select * from gongshang where password = %s "
        param2 = [password]
        data2 = select(sql2, param2)
        if len(data3)>=1 and len(data2)>=1:
            return 0
        elif len(data3)==0:
            return 1
        elif len(data2)==0:
                return 2

user=gongshang()
while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        user.useradd()
        print(bank)
    elif index ==2:
        print("存钱")
        user.cunqianadd()
    elif index ==3:
        print("取钱")
        user.quxianadd()
    elif index ==4:
        print("转账")
        user.zhuanzhangadd()
    elif index ==5:
        print("查询")
        user.chaxunadd()
    elif index ==6:
        print("下次光临")
        break
