
class CurvaBezier:

    def __init__(self, conj_pontos, bezier):
        self.conj_pontos = conj_pontos
        self.bezier = bezier
        self.passos = 100

        print(self.conj_pontos)

    def encontra_curva(self):
        i = 1
        self.bezier.append(self.conj_pontos[0])

        while i < self.passos+1: #i está guardando em qual iteração estou; começa no 1 pois já tenho ponto 0 da curva
            self.bezier.append(self.proximo_ponto(i))
            i = i+1

        self.bezier.append(self.conj_pontos[-1])

        return self.bezier

    def proximo_ponto(self, passo):
        r = len(self.conj_pontos)-1
        novo = self.conj_pontos.copy()
        t = (1.0/self.passos) * passo

        while r != 0:
            i = 0
            while i < r:

                coordX = ((1-t)*novo[i][0]) + (t*novo[i+1][0])
                coordY = ((1-t)*novo[i][1]) + (t*novo[i+1][1])
                coordZ = ((1-t)*novo[i][2]) + (t*novo[i+1][2])

                novo[i] = [coordX, coordY, coordZ]
                i = i+1

            r = r-1

        return novo[0]


