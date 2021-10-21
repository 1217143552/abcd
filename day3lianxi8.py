'''
使用while循环实现NxN乘法表的打印。
'''

i=1
while i<=9:
    j=1
    while j<=9:
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1

