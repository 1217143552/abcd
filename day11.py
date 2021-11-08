# 按要求定义类
# 考查知识点：super关键字的使用和继承中方法的调用
# 要求：
# 1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
# 2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
# 3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
# 4、使用新手机对象调用手机介绍的方法；
# 5、使用新手机对象调用打电话的方法；
# 1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
class oldphone:
    __brand= ""
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand
    def cell(self,num):
        print("正在给%s打电话"%num)
# 2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、
# “正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，
# 不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，
# 内容为：“品牌为：xxx的手机很好用...”
class newphone(oldphone):
    def Cell(self,number):
        print("语音拨号中...")
        print(self.cell(number))
    def showphone(self):
        print(self.getBrand(),"手机很好用")
# 3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
np=newphone()
np.setBrand("iphone")
# 4、使用新手机对象调用手机介绍的方法；
np.showphone()
# 5、使用新手机对象调用打电话的方法；
np.Cell(12345678910)
# 题目一：
# 考查知识点：继承的传递性
# 按要求定义类
# 要求：
# 1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
# 2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
# 3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
# 4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
# 5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；

# 1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，
# 提供无返回值的无参数的蒸饭方法；
class cook:
    __name=""
    __age=None
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def SteamedRice(self):
        print("正在蒸米饭")
# 2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
class Cooker(cook):
    def Cooking(self,name):
        self.setName(name)
        print(self.getName(),"将要炒菜")
# 3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
class cooker(Cooker):
    def steamedrice(self):
        print("蒸饭")
    def cooking(self):
        print("炒菜")
# 4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
cker1=cooker()
cker1.setName("张三")
cker1.setAge(30)
print(cker1.getName())
print(cker1.getAge())
# 5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；
cker2=cooker()
cker2.cooking()
cker2.SteamedRice()
cker2.steamedrice()
cker2.Cooking("李四")
# 请编程
# i.人：年龄，性别，姓名。
# ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
# iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

# i.人：年龄，性别，姓名。
class person:
    __name=""
    __sex=""
    __age=None
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age
# ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
class worker(person):
    def Work(self,name,age,work):
        self.setName(name)
        self.setAge(age)
        print("%s岁的%s正在做%s"%(age,name,work))
        print(self.getAge(),"岁的",self.getName(),"正在做",work)
# iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。
# 行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
class student(person):
    def sing(self,name,age,song):
        self.setName(name)
        self.setAge(age)
        print(self.getAge(),"岁的",self.getName(),"正在唱",song)

w=worker()
w.Work("马保国",69,"闪电五连鞭")