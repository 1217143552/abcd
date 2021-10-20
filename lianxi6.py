'''
练习6：输入三条边长，如果能构成三角形就计算周长和面积
提示：需要手动输入三条边长
'''
import math
print("请输入三边周长：")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

p=a+b+c

S=math.sqrt(p*(p-a)*(p-b)*(p-c))

print("面积：",S)
