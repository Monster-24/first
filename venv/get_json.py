import json

with open('data1.json','r') as file:
    str=file.read()
    data=json.loads(str)
    print(data)