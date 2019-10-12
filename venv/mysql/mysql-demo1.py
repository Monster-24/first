import pymysql

db=pymysql.connect(host='47.101.142.21',user='root',password='root',port=3306,db='spiders')
cursor=db.cursor()
cursor.execute('SELECT version()')
data=cursor.fetchone()
print('databaseVeison是：',data)

# 创建数据库
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
# 创建表
sql='CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'
cursor.execute(sql)
db.close()