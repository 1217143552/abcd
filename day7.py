import xlrd#引入Excel操作模块

workbook=xlrd.open_workbook(filename='2020.xlsx')
#1.1计算总销售额
for j in range(0,12):
#第j月
    table=workbook.sheet_by_index(j)#选择sheet
# rowd=table.row(0)#行
# cold=table.col(0)#列
# value=table.cell_value(0,0)#行列单元格
# print(rowd)
# print(cold)
# print(value)
    num=0#总销售额
    Sales=0#总销量
    yurongfu=niuzaiku=fengyi=picao=Txu=majia=0#百分比率
    for i in range(1,len(table.col(0))):
        Sales+=table.cell_value(i,4)
        num+=table.cell_value(i,2)*table.cell_value(i,4)
        if table.cell_value(i,1)=="羽绒服":
            yurongfu+=table.cell_value(i,4)
        elif table.cell_value(i,1)=="牛仔裤":
            niuzaiku+=table.cell_value(i,4)
        elif table.cell_value(i,1)=="风衣":
            fengyi+=table.cell_value(i,4)
        elif table.cell_value(i,1)=="皮草":
            picao+=table.cell_value(i,4)
        elif table.cell_value(i,1)=="T血":
            Txu+=table.cell_value(i,4)
        elif table.cell_value(i, 1) == "马甲":
            majia += table.cell_value(i,4)
    print("第%d月的总销售额是："%(j+1),"%.2f"%num)
    print("第%d月的平均销售量是："%(j+1),"%.2f"%(Sales/(len(table.col(0))-1)))
    print("羽绒服销量占的百分比：%0.2f%%"%(yurongfu/Sales))
    print("牛仔裤销量占的百分比：%0.2f%%"%(niuzaiku/Sales))
    print("风衣销量占的百分比：%0.2f%%"%(fengyi/Sales))
    print("皮草销量占的百分比：%0.2f%%"%(picao/Sales))
    print("T血销量占的百分比：%0.2f%%"%(Txu/Sales))
    print("马甲销量占的百分比：%0.2f%%"%(majia/Sales))

# import xlrd
# workbook=xlrd.open_workbook(filename='2020.xlsx')
# #计算每个种类月销售量占比
# for j in range(0,12):
#     table = workbook.sheet_by_index(j)
#     yurongfu=niuzaiku=fengyi=picao=Txu=majia=0
#     for i in range(1, len(table.col(0))):
#         if table.cell_value(i,1)=="羽绒服":
#             yurongfu+=table.cell_value(i,4)
#         elif table.cell_value(i,1)=="牛仔裤":
#             niuzaiku+=table.cell_value(i,4)
#         elif table.cell_value(i,1)=="风衣":
#             fengyi+=table.cell_value(i,4)
#         elif table.cell_value(i,1)=="皮草":
#             picao+=table.cell_value(i,4)
#         elif table.cell_value(i,1)=="T血":
#             Txu+=table.cell_value(i,4)
#         elif table.cell_value(i, 1) == "马甲":
#             majia += table.cell_value(i, 4)
#     print("羽绒服",yurongfu)
#     print("牛仔裤",niuzaiku)
#     print("风衣",fengyi)
#     print("皮草",picao)
#     print("T血",Txu)
#     print("马甲",majia)
