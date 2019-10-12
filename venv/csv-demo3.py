# import csv
import pandas as pd
# with open('data1.csv','r',encoding='utf-8') as csvfile:
#     read=csv.reader(csvfile)
#     for raw in read:
#         print(raw)
df=pd.read_csv('data1.csv')
print(df)

