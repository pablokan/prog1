import PySimpleGUI as sg
from random import randint

sg.theme('DarkAmber')

archivo = open('palabras.txt','r')
linea = archivo.read().split('\n')
palabra = linea[randint(0,len(linea)-1)].lower()
espacios = ['_'] * len(palabra)
guiones = ' '.join(espacios)
archivo.close()
intentos = 5
letrasFalladas = []
imagenes = ['1.png','2.png','3.png','4.png','5.png','6.png']

def inicio():
    layout = [
                [sg.T('Ahorcado',font=('Georgia 30'),text_color=('white'),pad=(0,20))],
                [sg.B('Jugar',button_color='#ffd424',bind_return_key=True,pad=(20,5),font=('Arial 20'))],
    ]
    return sg.Window('Inicio', layout=layout,size=(300,160),element_justification='center',grab_anywhere = True,finalize=True)

def juego():
    layout = [
                [sg.T(guiones,font=('Georgia 15'),text_color=('white'),key='-GUIONES-')],
                [sg.Image(imagenes[5],pad=(0,15),key='-IMAGENES-')],
                [sg.T('Ingrese una letra:',pad=(0,15),text_color=('white'),font=('Georgia')),sg.I(text_color=('white'),size=(2,0),font=('Georgia'),key='-SALIDA-'),sg.T(size=(40,1),text_color=('white'),key='-AVISO-')],
                [sg.T(font=('Georgia'),pad=(150,0),text_color=('white'),key='-LETRA_FALLADA-')],
                [sg.T(f'Intentos: {intentos}',pad=(0,15),font=('Georgia'),text_color=('white'),key='-INTENTOS-')],
                [sg.B('Enviar',button_color='#ffd424',bind_return_key=True,font=('Arial')),sg.B('Salir',button_color='#ffd424',font=('Arial'))],
    ]
    return sg.Window('Juego ahorcado',layout=layout,size=(400,500),element_justification='center',no_titlebar=True,grab_anywhere = True,finalize=True)

def ventanaGanadora():
    layout = [
        [sg.T('¡Ganaste!',text_color=('white'),font=('Georgia 15'))],
        [sg.Image('trofeo.png',size=(100,200))],
        [sg.B('Volver a jugar',button_color='#ffd424',bind_return_key=True,font=('Arial')),sg.B('Salir',button_color='#ffd424',font=('Arial'))],
    ]
    return sg.Window('Ganaste',layout=layout,element_justification='center',no_titlebar=True,grab_anywhere = True,finalize=True)

def ventanaPerdedora():
    layout = [
        [sg.T('¡Ahorcado!',text_color=('white'),font=('Georgia 15'))],
        [sg.Image('soga.png',size=(60,200))],
        [sg.B('Volver a jugar',button_color='#ffd424',bind_return_key=True,font=('Arial')),sg.B('Salir',button_color='#ffd424',font=('Arial'))],
    ]
    return sg.Window('Perdiste',layout=layout,element_justification='center',no_titlebar=True,grab_anywhere = True,finalize=True)

ventana = inicio()

while True:
    window,event,values = sg.read_all_windows()
    if event in [None, 'Salida'] or event == sg.WIN_CLOSED :
        break
    print(event,values)
    if event == 'Jugar':
        ventana2 = juego()
        ventana.hide()
    if event == 'Salir':
        break
    if event == 'Enviar':
        valor = values['-SALIDA-']
        letrasDisponibles = 'abcdefghijklmnñopqrstuvwxyzáéíóú'
        if (len(valor) != 1) or (valor not in letrasDisponibles):
            aviso = 'Debe ingresar una letra minuscula'
            window['-AVISO-'].update(aviso)
        else:
            aviso = ''
            window['-AVISO-'].update(aviso)
            estado = False
            for indice , caracter in enumerate(palabra):
                if caracter == valor:
                    espacios[indice] = valor
                    window['-GUIONES-'].update(value=' '.join(espacios))
                    estado = True

            if not estado:
                if intentos > 0 and valor not in palabra and valor not in letrasFalladas:
                    letrasFalladas.append(valor)
                    window['-LETRA_FALLADA-'].update(value=' '.join(letrasFalladas))
                    intentos -= 1
                    cambiaImag = imagenes[intentos]
                    window['-INTENTOS-'].update(value=f'Intentos: {intentos}')
                    window['-IMAGENES-'].update(cambiaImag)

            if '_' not in espacios:
                window.close()
                ventana3 = ventanaGanadora()

            if intentos == 0:
                window.close()
                ventana4 = ventanaPerdedora()

    elif event == 'Volver a jugar':
        window.close()
        ventana = inicio()
        intentos = 5
        palabra = linea[randint(0,len(linea)-1)].lower()
        espacios = ['_'] * len(palabra)
        guiones = ' '.join(espacios)
        letrasFalladas = []