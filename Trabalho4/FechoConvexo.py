# coding=utf-8

import math


class FechoConvexo:

    def __init__(self, conj_pontos):
        self.fecho_convexo = []
        self.conj_pontos = conj_pontos

    def jarvis(self):

        self.conj_pontos.sort(key=lambda k: k[1])  # Ordeando de maneira crescente a lisa de entrada deconjunto depontos
        self.fecho_convexo.append(self.conj_pontos[0]) #acho o p0 que representa o ponto inicial de menor coordenada y
        #acho o próximo ponto do meu fecho convexo;
        self.fecho_convexo.append(self.proximo(self.fecho_convexo[0], 1, 0)) #Sendo que estou passando o vetor [1, 0] que o vetor que sai do meu p0


        i = 1
        # Enquanto o próximo for diferente do primeiro, eu rodo o loop
        while self.fecho_convexo[i] != self.fecho_convexo[0]:

            # Achando o vetor que está entre o ponto que estou analisando e o candidato a próximo
            v1_x = self.fecho_convexo[i][0] - self.fecho_convexo[i-1][0] #coordenada x
            v1_y = self.fecho_convexo[i][1] - self.fecho_convexo[i-1][1] #coordenada y

            self.fecho_convexo.append(self.proximo(self.fecho_convexo[i], v1_x, v1_y)) #Assim analiso se o ponto é realmente válido para ser o próximo, se for adiciono a minha lista do fecho convexo
            i = i+1

        return self.fecho_convexo


    '''
        O retorno da função é o ponto que possui a menor angulação com o vetor.
    '''
    def proximo(self, ponto, v1_x, v1_y):
        # A variavel menor irá guardar o ponto que possui a angulação menor; Inicializada com -2, pois qualquer angulo será maior que esse
        cos_ant = -2

        #Varáve irá guarda as coordenadas do ponto que possui o menor angulo entre os vetores
        menor_x = 0 #Coordanada x
        menor_y = 0 #Coordenada y


        # Retorna um ponto p tal que o angulo de v1 e v2 (p0p) seja minimo
        i = 0
        while i < len(self.conj_pontos):

            # Se o ponto que estou analisando é o mesmo ponto que o loop está, não tem necessidade de fazer a conta, pois ele com certeza não será
            if ponto == self.conj_pontos[i]:
                pass

            #Caso seja diferente eu efetivamente faço a conta
            else:
                # Calculo o vetor entre o ponto que estou analisando com os outros pontos para analisar o angulo
                v2_x = self.conj_pontos[i][0] - ponto[0] #coordenada x
                v2_y = self.conj_pontos[i][1] - ponto[1] #coordenada y

                cos = self.angulo(v1_x, v1_y, v2_x, v2_y) #Calculo o cos entre v1 e v2 na busca do maior cos, que então será o menor angulo

                if cos > cos_ant: #Se o retorno qe eu tive for maior que o anterior significa que eu encontrei um ponto mais qualificado para o meu fecho convexo
                    cos_ant = cos # Se é mais qualificado eu troco
                    menor_x = self.conj_pontos[i][0] #E então a variável menor fica com o valor do ponto que o loop está olhando
                    menor_y = self.conj_pontos[i][1]

            i = i+1

        # Retorno em formato de lista para adicionar a minha lista de pontos
        return [menor_x, menor_y]


    '''
        Para calcular o angulo, iremos usar o Produto interno para achar o cos(teta);
        O angulo que tiver o maior cos(teta) será o próximo ponto, pois terá a angulação menor.
    
        Sendo v2 o vetor entre os dois pontos
    
        O retorno da função é cos(teta) entre o vetor que sai do ponto e o vetor que liga os pontos.
    '''
    def angulo(self, v1_x, v1_y, v2_x, v2_y):
        # Fórmula do Produto interno
        # cos(teta) = c = <v1,v2> / |v1||v2|

        norma_v1 = math.sqrt(v1_x ** 2 + v1_y ** 2)

        norma_v2 = math.sqrt(v2_x ** 2 + v2_y ** 2)

        cos = ((v1_x * v2_x) + (v1_y * v2_y)) / (norma_v1 * norma_v2)

        return cos
