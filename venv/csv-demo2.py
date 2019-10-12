import csv

with open('data1.csv','a',encoding='utf-8') as csvfile:
    filednames=['id','name','age']
    write=csv.DictWriter(csvfile,fieldnames=filednames)
    write.writeheader()
    write.writerow({'id':'10001','name':'monster','age':20})
    write.writerow({'id': '10002', 'name': '阿坤', 'age': 20})