import os
os.system('cls')


nombres=['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana', 'Santamaría, Carlos', 'Skarsgard, Azul', 'Catalejos, Walter']
fecNac=['02-05-1943',	'07-09-1984', '10-02-1971',	'21-12-1967', '30-01-1982', '30-08-1995',	'18-07-1959']
sexo=['f', 'f', 'm', 'f', 'm', 'f', 'm']
d=0
q=0
prom=0
año=2021
x=1
for i in range(len(nombres)):
    n=nombres[i]
    m=n.find(',')
    o=m+2
    apel=n[:m]
    print(n[o]+'.', apel)
    nom=n[o:]
    if len(nom)>d:
        long=nom
        d=len(nom)
    if sexo[i]=='f':
        q=q+1        
        f=fecNac[i]
        fe=int(f[6:])
        prom=prom+año-fe    
    if len(nom)>d:
        long=nom
        d=len(nom)
   
med=int(prom/q)       
print('El nombre mas largo es ', long, ' y tiene ', d, ' letras.' )       
print('El promedio de edad de las mujeres es :', med)


