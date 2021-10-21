'''
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''



for i in range(1,4):
    name=["root"]
    pwd=["admin"]
    username=[]
    userpwd=[]
    username.append(input("请输入用户名："))
    userpwd.append(input("请输入密码："))
    if username==name and userpwd==pwd:
        print("登录成功")
        break
    else:
        print("登录失败")
    if i==3:
        print("账户已锁定")