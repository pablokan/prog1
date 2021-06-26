d = {'name': 'juan', 'age': 31}
d['height'] = 1.89
del d['age'] #d.pop('age')
print(d)

if 'height' in d.keys():
    print(d['height'])

if 'juan' in d.values():
    print('ta juan')


