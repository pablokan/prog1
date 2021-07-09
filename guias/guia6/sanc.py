def inputMail(correo):
    imail = input(correo)
    dire=False
    while not dire:
        arroba=imail.find('@')
        punto=imail.find('.')
        if arroba>0 and punto-arroba>0:
                dire=True            
        else:
            print('Error. El correo debe contener una "@" y un servidor.')
            imail=input('Ingrese nuevamente el mail ')
    return imail

if __name__ == '__main__':
    email=inputMail('Ingrese su correo electrónico: ')
    print(email)