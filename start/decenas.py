num = input('Ingrese un número natural (entero positivo): ')
num = int(num) # conversión de tipo de dato: str -> int

if num < 10:
    print('primera decena')
elif num >=10 and num <20: # expresión con conector and
    print('segunda decena')
elif 20 <= num < 30: # otra forma de escribir la expresión 
    print('tercera decena')
else:
    print('30 o más grande')

    
