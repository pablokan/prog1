def concatenar_strings(separador=' '):
    """" Concatena numero indeterminado de strings con un caracter determinado"""
    frase = input('Ingrese frase a concatenar: ')
    result = ''
    while frase.lower() != 'fin':
        result = result + frase + separador
        frase = input('Ingrese frase a concatenar: ')
    # Devuelve la frase con el separador, menos el ultimo caracter.
    return result[0:-1]

testing = concatenar_strings()    
print(testing)


