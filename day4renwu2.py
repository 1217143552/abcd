'''
现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
[罗恩, 23 ,35 ,44]
[哈利 ,60, 77 ,68 ,88, 90]
[赫敏, 97 ,99 ,89 ,91, 95, 90]
[马尔福 ,100, 85 ,90]
求每个人的总成绩？
'''
name=[["罗恩", 23 ,35 ,44],
["哈利",60, 77 ,68 ,88, 90],
["赫敏", 97 ,99 ,89 ,91, 95, 90],
["马尔福",100,85,90]]
i=0
j=0
grade=0
for i in range(0,4):
    for j in range(1,len(name[i])):
        grade=grade+name[i][j]
    else:
        print(name[i][0], "grade is", grade)
        grade = 0
# if j==len(name[j]):
# print(name[i][0],"grade is",grade)