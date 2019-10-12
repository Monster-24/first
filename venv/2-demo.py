import json

str = '''
[{
   "name":"Monster",
   "gender":"male"
}]
'''
data=json.loads(str)
print(data)