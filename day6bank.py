import random
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
#初始化银行
bank={}
#'Frank': {'account': 24275182, 'password': '123456',
# 'country': '中国', 'province': '山东', 'steert': '曹县',
# 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="银行"

#定义数据限制函数
def bankadd(account,name,password,country,province,street,door):
    if len(bank)>=100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "steert":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1

#定义用户开户函数
def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入您的名称")
    password=input("请输入您的密码")
    print("请输入你的详细信息")
    country=input("\t\t请输入您的国籍")#\t ==tab
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,street,door)
    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，一下是您的相信信息")
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：*****
                   国籍：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province,
                      street, door,
                      bank[name]["money"], bank_name))

#定义存钱函数
def moneyAdd(account):
    for i in bank:
        if bank[i]["account"]==account:
            money = input("请输入存入金额")
            bank[i]["account"]+=money
            return True
        else:
            return False
def moneyadd():
    account=input("请输入您的账号")
    num1=moneyAdd(account)
    if num1==False:
        print("该用户不存在")
    elif num1==True:
        info = '''
                   ------------个人信息------------
                   用户名:%s               
                   密码：*****
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (account, bank[account]["money"], bank_name))


#定义取钱函数
def moneySubtract(account,password):
    money=input("请输入取出金额")
    for i in bank:
        if bank[i]["account"] != account:
            return 1
        elif bank[i]["account"] == account and bank[i]["password"]!=password:
            return 2
        elif bank[i]["account"] == account and\
            bank[i]["password"]==password and\
            bank[i]["money"]<money:
            return 3
        elif bank[i]["account"] == account and\
            bank[i]["password"]==password and\
            bank[i]["money"]>=money:
            bank[i]["money"]-=money
            return 0
def moneysubtract():
    account = input("请输入账号")
    password=input("请输入密码")
    num2=moneySubtract(account,password)
    if num2==1:
        print("账号不存在")
    elif num2==2:
        print("密码错误")
    elif num2==3:
        print("余额不足")
    elif num2==0:
        info = '''
                   ------------个人信息------------
                   用户名:%s               
                   密码：*****
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (account, bank[account]["money"], bank_name))

#定义转账函数
def moneyTransfer(account1,account2,password):
    if account1 in bank and account2 in bank:
        if password == bank[account1]['password']:
            money = int(input("请输入您要转出的金额："))
            money = bank[account1]['money'] - money
            if money < 0:
                return 3
            elif money >= 0:
                bank[account1]['money'] = money
                bank[account2]['money'] = money
                return 0

    if account1 not in bank or account2 not in bank:
        return 1
    elif password != bank[account1]['password']:
        return 2
def moneytransfer():
    account1 = input("请输入账号")
    account2 = input("请输入账号")
    password = input("请输入密码")
    num3 = moneyTransfer(account1,account2,password)
    if num3 == 1:
        print("账号不存在")
    elif num3 == 2:
        print("密码错误")
    elif num3 == 3:
        print("余额不足")
    elif num3 == 0:
        info = '''
                   ------------个人信息------------
                   用户名:%s               
                   密码：*****
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (account1, bank[account1]["money"], bank_name))

#定义查询函数
def query():
    account=print("请输入账号")
    password=print("请输入密码")
    for i in bank:
        if bank[i]["account"] != account:
            print("账户不存在")
        else:
            if bank[i]["password"] != password:
                print("密码错误")
            else:
                info = '''
                                   ------------个人信息------------
                                   用户名:%s               
                                   密码：*****
                                   余额：%s
                                   开户行名称：%s
                               '''
                # 每个元素都可传入%
                print(info % (account, bank[account]["money"], bank_name))

while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        useradd()
        print(bank)
    elif index ==2:
        print("存钱")
        moneyadd()
    elif index ==3:
        print("取钱")
        moneysubtract()
    elif index ==4:
        print("转账")
        moneytransfer()
    elif index ==5:
        print("查询")
        query()
    elif index ==6:
        print("下次光临")
        break
