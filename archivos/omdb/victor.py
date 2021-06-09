json = open('omdb/pelis.json', 'r')
c = 'nada'
aux =''
control = True
while c != '' and control:
    c = json.read(1)
    if c == 'T':
        json.seek(json.tell() + 8)
        comT = json.tell()
        c = ''
        while c != '"':
            aux = aux + c
            c = json.read(1)
            control = False
print(aux)
json.close()  
