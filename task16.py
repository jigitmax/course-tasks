import json
dict1 = {'first': 123, 'second': 3.2, 'third': True, 'fourth': 'abc'}
str_json = json.dumps(dict1)
print(str_json)
print(type(str_json))