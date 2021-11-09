import pymysql

host="localhost"
user="root"
pwd = ""
database="bank"

# 针对增，删，改
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=pwd,database=database)#建立连接

    cursor = con.cursor()#创建光标
    cursor.execute(sql,param)#execute执行sql语句

    con.commit()#提交到数据库
    cursor.close()
    con.close()

#针对查询语句的函数
def select(sql,param,mode="all",size=0):
    con = pymysql.connect(host=host,user=user,password=pwd,database=database)

    cursor = con.cursor()
    cursor.execute(sql,param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()




















