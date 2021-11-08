# 题目一：
# 该题考查点：属性和方法的使用！
# 定义一个空调类和对应的测试类
# 要求：
# 1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
# 2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
# 3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，内容打印一句话：“空调将在xxx分钟后自动关闭...”；
# 4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
# 5、使用空调对象获取空调的品牌和价格并打印到控制台上；
# 6、使用空调对象调用开机方法；
# 7、使用空调对象调用定时关机方法，并传递具体数据值，在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
# 其中语句中的“xxx”是调用方法时传递的具体数据值；

class airConditioner:
    __brand=""
    __price=0

    #1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
    def setprice(self,price):
        if price<0:
            print("宁赔本赚吆喝")
        else:
            self.__price = price
    def getprice(self):
        return self.__price
    def setbrand(self,brand):#给品牌赋值
        self.__brand = brand
    def getbrand(self):
        return self.__brand

    #2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
    def start(self):
        print("空调开机了")

    def close(self,time):
        print("空调在",time,"分钟后关闭")
    #3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，内容打印一句话：“空调将在xxx分钟后自动关闭...”；
    # def offTime(self,time):
    #     time=sleep(60/60)
    #     print("空调将在", time, "分钟后自动关闭")

    #4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
    #5、使用空调对象获取空调的品牌和价格并打印到控制台上；
airconditioner=airConditioner()
airconditioner.setbrand("格力")
airconditioner.getbrand()
airconditioner.setprice(5000)
airconditioner.getprice()
# 6、使用空调对象调用开机方法；
airconditioner.start()
# 7、使用空调对象调用定时关机方法，并传递具体数据值，在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
airconditioner.close(1)

# 题目二：
# 该题考查点：self关键字的使用！
# 定义一个学生类和对应的测试类
# 要求：
# 1、学生有姓名和年龄两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
# 2、提供一个无返回值的无参数的自我介绍的方法，内容打印一句话：
# “大家好，我叫xxx，今年xxx岁了！”
# 3、提供一个返回值为String类型，参数为学生类型的比较年龄差值的方法，如果当前对象的年龄比参数中的学生的年龄大，则返回：“我比同桌大xxx岁！”；如果当前对象的年龄比参数中的学生的年龄小，则返回：“我比同桌小xxx岁！”；如果当前对象的年龄和参数中的学生的年龄一样大，则返回：“我和同桌一样大！”
# 4、在测试类中分别创建你和你同桌两个人的对象，并分别给你和你同桌的姓名和年龄属性赋上对应的值；
# 5、调用你自己的对象的自我介绍的方法，展示出你自己的姓名和年龄；
# 6、用你自己的对象调用比较年龄差值的方法，把你同桌作为参数使用，并打印方法返回的字符串的内容；
#
class student:
    __name=None
    __age=None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        if age<17 or age>25:
            print("你是高中生或毕业了？")
        else:
            self.__age = age
    def getAge(self):
        return self.__age

    def ShowMe(self):
        print("大家好，我叫",self.__name,"，今年",self.__age,"岁了")

    def compare(self, student):
        if self.__age > student.getAge():
            print("我比同桌大",(self.__age - student.getAge()),"岁！")
        elif self.__age < student.getAge():
            print("我比同桌小", ( student.getAge()- self.__age),"岁！")
        else:
            print("我俩一样大！")

s1=student()
s1.setName("张三")
s1.setAge(22)
s1.ShowMe()
s2=student()
s2.setName("李四")
s2.setAge(20)
s2.ShowMe()
s1.compare(s2)

# 题目三：打电话业务逻辑
# 人类：
# 属性:
# 姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分。
# 功能：
# 发短信（要求参数传入短信内容）。
# 打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否小于1元，若为空或者小于1元则报相对应的错误信息，否则的话拨通。结束后，按照时间长度扣费并返回扣费（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟））
class People:
    __name = ''
    __gender = ''
    __age = 0
    __cost = 0   # 剩余话费
    __brand = ''   # 品牌
    __battery = 0  # 电池容量
    __size = 0    # 屏幕大小
    __standby = 0   # 最大待机时长
    __integral = 0  # 积分

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setAge(self, age):
        if age <= 0 or age >= 120:
            print('年龄非法！')
        else:
            self.__age = int(age)

    def getAge(self):
        return self.__age

    def setCost(self, cost):
        self.__cost = float(cost)

    def getCost(self):
        return self.__cost

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setBattery(self, battery):
        if battery < 0:
            print('电池容量不能为负！')
        else:
            self.__battery = float(battery)

    def getBattery(self):
        return self.__battery

    def setSize(self, size):
        if size <= 0:
            print('屏幕大小输入非法！')
        else:
            self.__size = int(size)

    def getSize(self):
        return self.__size

    def setStandby(self,standby):
        self.__standby = int(standby)

    def getStandby(self):
        return self.__standby

    def setIntegral(self, integral):
        if integral < 0:
            print('积分不能为负！')
        else:
            self.__integral = int(integral)

    def getIntegral(self):
        return self.__integral

    def show(self):
        print('姓名', self.__name, '\n性别', self.__gender, '\n年龄', self.__age,'\n所拥有的手机剩余话费',
              self.__cost, '元！\n手机品牌', self.__brand,'\n手机电池容量', self.__battery, '%\n屏幕大小',
              self.__size, '寸\n最大待机时长',self.__standby, '分钟\n所拥有积分：', self.__integral)


p = People()
p.setName(input('输入姓名'))
p.setGender(input('输入性别'))
p.setAge(int(input('输入年龄')))
p.setCost(float(input('输入手机剩余话费')))
p.setBrand(input('输入手机品牌'))
p.setBattery(float(input('输入电池容量')))
p.setSize(int(input('输入手机屏幕大小')))
p.setStandby(int(input('输入手机最大待机时长')))
p.setIntegral(int(input('输入拥有积分')))
p.show()
cc = p.getCost()
dd = p.getIntegral()

while True:
    a = int(input('需要打电话还是发短信：（1或2）'))
    if a == 1:
        a_1 = input('输入短信内容：')
        print('短信内容为：\n', a_1)
    elif a == 2:
        a_1 = int(input('输入电话号码：'))
        a_2 = int(input('输入打多长时间：'))
        if a_1 == None: print('不能为空！')
        elif a_1 <= 1: print('电话费不够了！')
        else:
            print('电话已拨通！')
        if a_2 >= 0 and a_2 <= 10:
            if dd >= a_2 * 15:
                dd -= a_2 * 15
            else:
                cc -= a_2 * 1
        elif a_2 > 10 and a_2 <=20:
            if dd >= a_2 * 39:
                dd -= a_2 * 39
            else:
                cc -= a_2 * 0.8
        else:
            if dd >= a_2 * 48:
                dd -= a_2 * 48
            else:
                cc -= a_2 * 0.65

        print('剩余话费为：', cc)
        print('剩余积分为：', dd)

#1定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。行为：学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名），编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）
class Student:
    __snum = 0
    __name = ""
    __age = 0
    __sex = ""
    __high = 0
    __weight = 0
    __grade = 0
    __address = ""
    __phone = 0

    def set_snum(self, num):
        self.__snum = num
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_sex(self, sex):
        self.__sex = sex
    def set_high(self, high):
        self.__high = high
    def set_weight(self, weight):
        self.__weight = weight
    def set_grade(self, grade):
        self.__grade = grade
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone
    def get_snum(self):
        return self.__snum
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_sex(self):
        return self.__sex
    def get_high(self):
        return self.__high
    def get_weight(self):
        return self.__weight
    def get_grade(self):
        return  self.__grade
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone
    def study(self, time):
        print("学习了", time, "小时")
    def play_game(self, name):
        print("玩", name)
    def program(self, line):
        print("敲了", line, "行代码")
    def sum(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum

student = Student()
student.study(4)
student.program(50)
print(student.sum(1, 2))
student.play_game("lol")

# ii.车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。功能：跑（要求参数传入车的具体功能，比如越野，赛车）
# 创建：法拉利，宝马，铃木，五菱，拖拉机对象
class car:
    __type=""
    __num=0
    __color=""
    __weight=0
    __volume=0

    def setType(self,type):
        self.__type=type
    def getType(self):
        return self.__type

    def setNum(self,num):
        self.__num=num
    def getNum(self):
        return self.__num

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        self.__weight=weight
    def getWeight(self):
        return self.__weight

    def setVolume(self,volume):
        self.__volume=volume
    def getVolume(self):
        return self.__volume

    def Run(self,r_type):
        print(self.__type,"正在",r_type)
c1=car()
c1.setType("法拉利")
c2=car()
c2.setType("宝马")
c3=car()
c3.setType("铃木")
c4=car()
c4.setType("五菱")
c5=car()
c5.setType("拖拉机")

# iii.笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公。
class computer:
    __type=""
    __standby=""
    __color=""
    __weight=0
    __cputype=""
    __memory=0
    __volume=0

    def setType(self,type):
        self.__type=type
    def getType(self):
        return self.__type

    def setstandby(self,time):
        self.__standby=time
    def getstandby(self):
        return self.__standby

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        self.__weight=weight
    def getWeight(self):
        return self.__weight

    def setCPUType(self,type):
        self.__cputype=type
    def getCPUType(self):
        return self.__cputype

    def setmemory(self,memory):
        self.__memory=memory
    def getmemory(self):
        return self.__memory

    def setVolume(self,volume):
        self.__volume=volume
    def getVolume(self):
        return self.__volume

    def playgames(self,gamename):
        print(self.__type,"打",gamename,"游戏")

    def work(self,a):
        print("正在办公")

# iv.猴子类：属性：类别，性别，身体颜色，体重。行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
class Monkey:
    __type = ""
    __sex = ""
    __color = ""
    __weight = 0

    def set_type(self, name):
        self.__type = name
    def set_color(self, age):
        self.__color = age
    def set_weight(self, weight):
        self.__weight = weight
    def set_sex(self, grade):
        self.__sex = grade
    def get_sex(self):
        return self.__sex
    def get_type(self):
        return self.__type
    def get_color(self):
        return self.__color
    def get_weight(self):
        return self.__weight

    def study(self, name):
        print("正在学习",name)
    def make_fire(self, m):
        print("正在用", m, "造火")
monkey = Monkey()
monkey.study("钓鱼")
monkey.make_fire("木棍")