'''
有下列人员数据库，请按要求实现
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
1.统计每个人的平均薪资
2.统计每个人的平均年龄
3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
4.统计公司男女人数
5.每个部门的人数
'''
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
#1、统计平均薪资
i=0
S=0
for i in range(0,len(names)):
    S=S+names[i][5]
print("averS=",S/len(names))

#2.统计平均年龄
age=0
for i in range(0,len(names)):
    age=age+eval(names[i][1])
print("averAge=",age/(len(names)))

#3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
names.append(["刘备","45","男","220","alibaba",500,"30"])
print(names)

#4.统计公司男女人数
man=0
lady=0
for i in range(0,len(names)):
    if names[i][2]=="男":
        man=man+1
    else:
        lady=lady+1
print("man=",man)
print("lady=",lady)

#5.每个部门的人数
# department=0
# Num=0
# for i in range(0,len(names)):

