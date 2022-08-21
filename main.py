import eel
import simplekml
from random import randint


@eel.expose
class Terreno:
    def __init__(self):
        # Instanciando a lista vazia e contador
        self.nonce = ''
        self.pontos = []
        self.i = 0
        self.kml = simplekml.Kml()
    # Criando e dissolvendo as coordenadas em lista

    @eel.expose
    def inputCoordenadas(self, coordenadas):
        coordenadas = coordenadas.split('/')

        return coordenadas

    # Formando o laço de repetição para separar os pares e formatá-los
    @eel.expose
    def formatarLista(self, lista):
        for t in lista:
            t = t.split(',')
            t = [float(x) for x in t]
            self.pontos.append(t)
            self.i += 1

        return self.pontos
    # Adicionando todas as coordenadas em um único poligono e salvando e um arquivo.kml

    @eel.expose
    def salvarPoly(self, coordenadas):
        self.nonce = randint(1, self.i)
        self.kml.newpolygon(name=f'Terreno {self.i} pts',
                            outerboundaryis=coordenadas)
        self.kml.save(f'terreno-0{(self.i + self.nonce)**2}.kml')
        return True


eel.init('web')


@eel.expose
def generate(cords):
    terreno = Terreno()
    cords = terreno.inputCoordenadas(cords)
    listaf = terreno.formatarLista(cords)
    terreno.salvarPoly(listaf)


eel.start('index.html', size=(1280, 720), mode='chrome')
