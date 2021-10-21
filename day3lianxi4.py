'''
从键盘输入任意三边，
判断是否能形成三角形，若可以，则判断形成什么三角形
（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''

a=int(input("三角形边a="))
b=int(input("三角形边b="))
c=int(input("三角形边c="))

if a+b<=c or b+c<=a or a+c<=b:
    print("不能构成三角形")
else:
    if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("直角三角形")
    elif a==b and a!=c\
        or \
        b==c and b!=a\
        or \
        c==a and c!=b:
        print("等腰三角形")
    elif a==b and b==c:
        print("等边三角形")
    else:
        print("普通三角形")