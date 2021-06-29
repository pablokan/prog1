def crearArchivo(nombreArchivo):
    archivo = open(nombreArchivo,"w")
    archivo.close()

def guardarInfoEnTexto(infoAguardar,nombreArchivo):
    archivo = open(nombreArchivo,"a")
    archivo.write(infoAguardar + ",")
    archivo.close()

def leerInfoTexto (nombreArchivo):
    archivo = open(nombreArchivo,"r")
    info = archivo.read()
    archivo.close()
    return info

def leerLineaTexto (nombreArchivo):
    archivo = open(nombreArchivo,"r")
    info = archivo.readlines()
    archivo.close()
    return info
