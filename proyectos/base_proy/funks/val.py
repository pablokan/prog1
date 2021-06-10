def inputNumber(tipo, mensaje):
    validado = False
    numero = ""
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero":
                numero = int(numero)
            elif tipo == "real":
                numero = float(numero)
            else:
                print("Check! entero o real. Ctrl C!")
            validado = True
        except:
            print("Error. Debe ingresar un número", tipo)
    return numero

def inputMail(mensaje):
    validado = False
    mail = ""
    while not validado:
        mail = input(mensaje)
        if mail.count("@") == 1 and not(mail.startswith("@")) and not(mail.endswith("@")): # ok de arrobas
            front_back = mail.split("@")
            front, back = front_back
            if front[0].isalpha() and back.find(".") != -1:
                validado = True
        if not(validado):
            print("Error. No es una dirección de correo válida")
    return mail        
 
if __name__ == "__main__":
     a = inputMail('Correo: ')


