def crearArchivo(nombreArchivo):
    nomTxt = nombreArchivo + ".txt"
    archivo = open(nomTxt,"w")
    archivo.close()
def guardarInfoEnTexto(infoAguardar,nombreArchivo):
    nomTxt = nombreArchivo + ".txt"
    archivo = open(nomTxt,"a")
    archivo.write(infoAguardar + ",")
    archivo.close()
def leerInfoTexto (nombreArchivo):
    nomTxt = nombreArchivo + ".txt"
    archivo = open(nomTxt,"r")
    info = archivo.read()
    archivo.close()
    return info