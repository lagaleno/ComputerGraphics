
class CurvaBezier:

    def __init__(self, conj_pontos, bezier):
        self.conj_pontos = conj_pontos
        self.bezier = bezier
        self.passos = 200


    def encontra_curva(self):
        i = 1
        self.bezier.append(self.conj_pontos[0]) #garantindo quea minha curva vai ter o mesmo primeiro ponto que o meu poligono

        while i < self.passos+1: #i está guardando em qual iteração estou; começa no 1 pois já tenho ponto 0 da curva
            self.bezier.append(self.proximo_ponto(i))
            i = i+1

        self.bezier.append(self.conj_pontos[-1]) #garantindo que a minha curva vai ter o mesmo último ponto que meu poligono

        return self.bezier

    def proximo_ponto(self, passo):
        r = len(self.conj_pontos)-1
        novo = self.conj_pontos.copy()

        t = (1.0/self.passos) * passo #o t mostra o quanto estou caminhando entre um ponto e outro

        while r != 0:
            i = 0
            while i < r:


                coordX = ((1-t)*novo[i][0]) + (t*novo[i+1][0])
                coordY = ((1-t)*novo[i][1]) + (t*novo[i+1][1])
                coordZ = ((1-t)*novo[i][2]) + (t*novo[i+1][2])

                novo[i] = [coordX, coordY, coordZ]
                i = i+1

            r = r-1 # é como se estivesse tirando um dos pontos que estava no meu conj_pontos e analisando os outros

        #O ponto que queremos de fato vai estar na primeira posição da lista novo, após as iterações
        return novo[0]


