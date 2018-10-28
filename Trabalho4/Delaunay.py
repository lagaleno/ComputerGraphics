from FechoConvexo import FechoConvexo

class Delaunay:

    def __init__(self, conj_pontos):
        self.conj_pontos = conj_pontos

    def encontraTriangulo(self):
        self.encontraFecho()


    def encontraFecho(self):
        self.fechoConvexo = FechoConvexo(self.conj_pontos)

        self.poligono = self.fechoConvexo.jarvis()

        print(self.poligono)