# polimorfismo
class Perro:
    def sonido(self):
        print('Guauuuuu!!!')

class Gato:
    def sonido(self):
        print('Miaaauuuu!!!')
        
class Vaca:
    def sonido(self):
        print('Múuuuuuuu!!!')

if __name__ == '__main__':
    granja = [Gato(), Perro(), Gato(), Vaca()]
    for animal in granja:
        animal.sonido()
    