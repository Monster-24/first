import pymysql

data={
    "id":"10001",
    "name":"monster",
    "age":12
}
#连接数据库
db=pymysql.connect(host='47.101.142.21',user='root',password='root',port=3306,db='spiders')
#利用cursor来获取到操作游标
cursor=db.cursor()
table="students"
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql="INSERT INTO {table}({keys}) VALUES ({values})".format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('successful')
        print('github')
        db.commit()
except:
    print('failed')
    db.rollback()




# for raw in values:
#     print(raw)
