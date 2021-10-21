'''
实现输入10个数字，并打印10个数的求和结果
'''

num=[]
i=1
S=0
while i<=10:
    dint=int(input("请输入一个数字"))
    num.append(dint)
    S=S+dint
    i=i+1
print("10个数",num)
print("求和",S)