from json import loads, dumps

j = '{"name": "John", "age": null, "active": true}'
k = loads(j) # convierte la string JSON en un diccionario de Python
print(k)

users = [
    {"user": "juan", "active": True, "quota": None},
    {"user": "ana", "active": False, "quota": 300},
]
print(dumps(users, indent=2)) # operación contraria al loads, de dict a JSON
str_json = dumps(users)
print(type(str_json), str_json)



