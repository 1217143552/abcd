'''
用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''

n=int(input("输入阶乘数："))

A=1
S=0
for i in range(1,n+1):
    A=i*A
    S=S+A
print(A)
print(S)