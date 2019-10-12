import csv

with open('data.csv','w') as  csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerows([['1001','Monster','22'],['1002','Monster','22'],['1002','Monster','22']])
