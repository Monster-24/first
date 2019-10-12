import pymysql

id="20108181"
name="monster"
age=17
#连接数据库
db=pymysql.connect(host='47.101.142.21',user='root',password='root',port=3306,db='spiders')
#利用cursor来获取到操作游标
cursor=db.cursor()
sql="INSERT INTO students (id,name,age) values(%s,%s,%s)"
#执行sql语句。加了一层事务回滚，如何执行失败，就会执行rollback，相当于什么都没发生过
try:
    cursor.execute(sql,(id,name,age))
    db.commit()
except:
    db.rollback()
db.close()