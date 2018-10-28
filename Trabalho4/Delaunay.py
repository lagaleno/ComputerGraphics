import numpy
from math import sqrt


class Delaunay:
    def __init__(self, center=(0, 0), radius=9999):
        #Centro e raio para o super triangulo
        #Opcionais, coloquei o centro em 0,0 e raio 9999 para ter certeza de englobar todos

        center = numpy.asarray(center)

        # Cria coordenadas pra os cantos do frame em que o super triangulo se encontra
        self.cantos = [center+radius*numpy.array((-1, -1)),
                       center+radius*numpy.array((+1, -1)),
                       center+radius*numpy.array((+1, +1)),
                       center+radius*numpy.array((-1, +1))]

        # Create dois dicionarios para armazenar vizinhanca dos triangulo e circulos
        self.triangulos = {}
        self.circulos = {}

        T1 = (0, 1, 3)
        T2 = (2, 3, 1)
        self.triangulos[T1] = [T2, None, None]
        self.triangulos[T2] = [T1, None, None]

        # Computa centro e raio do circulo para cada triangulo
        for t in self.triangulos:
            self.circulos[t] = self.circumcentro(t)

    def circumcentro(self, tri):
        #Computa centro e raio da circunferencia
        pts = numpy.asarray([self.cantos[v] for v in tri])
        pts2 = numpy.dot(pts, pts.T)
        A = numpy.bmat([[2 * pts2, [[1],
                                 [1],
                                 [1]]],
                      [[[1, 1, 1, 0]]]])

        b = numpy.hstack((numpy.sum(pts * pts, axis=1), [1]))
        x = numpy.linalg.solve(A, b)
        bar_cantos = x[:-1]
        centro = numpy.dot(bar_cantos, pts)

        raio = numpy.sum(numpy.square(pts[0] - centro))  # Distancia ao quadrado
        return (centro, raio)

    def dentroCirculo(self, tri, p):
        #Checa se o ponto p esta dentro da circunferencia do triangulo tri
        centro, raio = self.circulos[tri]
        return numpy.sum(numpy.square(centro - p)) <= raio

    def adicionaPonto(self, p):
        #Adiciona ponto na triangulação
        p = numpy.asarray(p)
        #print(p)

        idx = len(self.cantos)
        self.cantos.append(p)

        # Procura triangulos ruins em que o circulo contem p
        bad_triangulos = []
        for T in self.triangulos:
            if self.dentroCirculo(T, p):
                bad_triangulos.append(T)

        #Borda do fecho convexo
        bordo = []
        # Escolhe um triangulo e uma aresta
        T = bad_triangulos[0]
        aresta = 0
        # Pega o triangulo oposto da aresta
        while True:
            # Checa se aresta do triangulo T esta no bordo
            tri_op = self.triangulos[T][aresta]
            if tri_op not in bad_triangulos:
                # Insere aresta e triangulo externo na lista do bordo
                bordo.append((T[(aresta+1) % 3], T[(aresta-1) % 3], tri_op))

                aresta = (aresta + 1) % 3

                # Checa se bordo fez loop
                if bordo[0][0] == bordo[-1][1]:
                    break
            else:
                aresta = (self.triangulos[tri_op].index(T) + 1) % 3
                T = tri_op

        # Remove triangulos muito proximos de p
        for T in bad_triangulos:
            del self.triangulos[T]
            del self.circulos[T]

        # Retriangula buracos deixadospor triangulos ruins
        novos_triangulos = []
        for (a0, a1, tri_op) in bordo:
            # Cria novo triangulo usando ponto p e arestas extremas
            T = (idx, a0, a1)
            #Guarda centro e raio do triangulo
            self.circulos[T] = self.circumcentro(T)
            self.triangulos[T] = [tri_op, None, None]

            # Tenta deixar T como vizinho do triangulo oposto
            if tri_op:
                # Procura vizinho de tri_op que usa aresta (a1, a0)
                for i, neigh in enumerate(self.triangulos[tri_op]):
                    if neigh:
                        if a1 in neigh and a0 in neigh:
                            self.triangulos[tri_op][i] = T

            # Adiciona triangulos numa lista temporaria
            novos_triangulos.append(T)

        # Liga novos triangulos com cada um
        N = len(novos_triangulos)
        for i, T in enumerate(novos_triangulos):
            self.triangulos[T][1] = novos_triangulos[(i+1) % N]   # proximo
            self.triangulos[T][2] = novos_triangulos[(i-1) % N]   # anterior

    def pegaTriangulos(self):
        return [(a-4, b-4, c-4)
                for (a, b, c) in self.triangulos if a > 3 and b > 3 and c > 3]