'''
请对下列列表进行冒泡排序（网易测试开发笔试题）
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
'''
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]

i,j=0,0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)