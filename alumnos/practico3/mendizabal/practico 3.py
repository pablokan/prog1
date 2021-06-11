from calcula_edad import edad
 
h = open("name.txt","r")

j = h.readlines()

h.close()

j1 = j[0]
j2 = j[1]
j1 = j1.split (",")
j2 = j2.split (",")

for z in range (len(j[:-1])):
    if edad(j2[z]) >= 18 :
        print(j1[z], "es mayor")
