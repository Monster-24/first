import json

str = '''
[{
   "name":"json",
   "birthday:"2019-01-10"
},{
   "name":"hello",
   "birthday":"2019-1-09"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
