'''
从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''

num=[]

i=1
S=0
while i<=10:
    dint=int(input("请输入一个整数"))
    num.append(dint)
    S=S+dint
    i = i + 1
print("和：",S)
print("平均值：",S/len(num))

for n in range(len(num)-1):
    if num[n]>=num[n+1]:
        c=num[n]
    else:
        c=num[n+1]
print("最大值：",c)