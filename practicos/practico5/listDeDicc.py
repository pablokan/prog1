from json import loads

stringDeJson = '[ {"uno": 1}, {"dos": 2} ]'

d = loads(stringDeJson)

print(d)
