import json

data=[{
    'name':'啊坤',
    'gender':'男',
    'birthday':'1992-10-18'
}]

with open('data1.json','a') as file:
    file.write(json.dumps(data,indent=5,ensure_ascii=False))