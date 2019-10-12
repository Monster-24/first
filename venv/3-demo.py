import json

str='''
[{
   "name":"Monster",
   "gender":"male"
   },{
   "name":"Monster12",
   "gender":"female"
}]
'''

print(type(str))
data=json.loads(str)
print(data)
print(type(data))
print(data[1].get('age'),24)
print(data)