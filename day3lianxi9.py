'''
编程实现99乘法表的倒叙打印
'''

i=1
for i in range(1,10):
    j=9
    while j>0:
        print(i,"*",j,"=",i*j)
        j=j-1