nombres_completos = ['Torres, Ana','Hudson, Kate','Quesada, Benicio','Campoamores, Susana','Santamaría, Carlos','Skarsgard, Azul','Catalejos, Walter']
sexos = ['f', 'f', 'm', 'f', 'm', 'f', 'm']
fechas_naci = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']

sobrantes = ['na','ate','enicio','usana','arlos','zul','alter']

a = (nombres_completos[0].split(sobrantes[0]))
b = (nombres_completos[1].split(sobrantes[1]))
c = (nombres_completos[2].split(sobrantes[2]))
d = (nombres_completos[3].split(sobrantes[3]))
e = (nombres_completos[4].split(sobrantes[4]))
f = (nombres_completos[5].split(sobrantes[5]))
g = (nombres_completos[6].split(sobrantes[6]))
suma_nombres = a + b + c + d + e + f + g
