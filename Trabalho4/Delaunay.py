from FechoConvexo import FechoConvexo
import math

class Delaunay:

    def __init__(self, conj_pontos, poligono):
        self.conj_pontos = conj_pontos
        self.poligono = poligono
        self.he = []
        self.visitar = []

    def encontraTriangulo(self):
        self.poligono = self.encontraFecho()

        #Encontrando o primeiro triangulo a partir do maior angulo
        #que a primeira aresta do poligono do fecho convexo faz
        vertice = self.encontraMaiorAngulo(self.poligono[0], self.poligono[1])

        #Adiciono o primeiro Triangulo na estrutura Half edge
        self.he.append(self.poligono[0])
        self.he.append(self.poligono[1])
        self.he.append(vertice)

        #Estrutura "triangulo" auxiliar para ajudar no desenho, de forma que eu feche o triangulo
        triangulos = self.he.copy()
        triangulos.append(self.he[0])

        #Adicionando na fila visitar as arestas que não pertencem ao Fecho Convexo
        self.visitar.append([self.he[1], self.he[2]])
        self.visitar.append([self.he[2], self.he[0]])


        i = 0
        while len(self.visitar) != 0:
            print(i)
            vertice = self.encontraMaiorAngulo(self.visitar[i][0], self.visitar[i][1])

            self.he.append(self.visitar[i][0])
            self.he.append(self.visitar[i][1])
            self.he.append(vertice)

            triangulos = self.he.copy()
            triangulos.append(self.visitar[i][0])

            self.visitar.remove(self.visitar[0])
            print(self.visitar)

            #adicionando as arestar que o programa deve visitar
            j = 0
            while len(self.poligono) > j:
                #Testo para adicionar as arestas qu NÃO pertencem ao fecho convexo para visitar

                if j < len(self.poligono) and self.he[-3] == self.poligono[j] and self.he[-2] == self.poligono[j+1]:
                    
                    pass #significa que essa aresta está no fecho convexo

                elif j < len(self.poligono) and self.he[-2] == self.poligono[j] and self.he[-1] == self.poligono[j+1]:
                    pass  # significa que essa aresta está no fecho convexo

                elif j < len(self.poligono) and self.he[-1] == self.poligono[j] and self.he[-3] == self.poligono[j+1]:
                    pass

        return triangulos

    def encontraFecho(self):
        print(self.poligono)
        return self.poligono


    def encontraMaiorAngulo(self, p_1, p_2):
        cos_ant = 2

        # Varáve irá guarda as coordenadas do ponto que possui o maior angulo entre os vetores
        maior_x = 0  # Coordanada x
        maior_y = 0  # Coordenada y


        i = 0
        while i < len(self.conj_pontos):

            if p_1 == self.conj_pontos[i] or p_2 == self.conj_pontos[i]:
                pass

            # Caso seja diferente eu efetivamente faço a conta
            else:
                # Calculo o vetor entre o ponto que estou analisando com os outros pontos para analisar o angulo
                v1_x = self.conj_pontos[i][0] - p_1[0]
                v1_y = self.conj_pontos[i][1] - p_1[1]

                v2_x = self.conj_pontos[i][0] - p_2[0]  # coordenada x
                v2_y = self.conj_pontos[i][1] - p_2[1]  # coordenada y

                cos = self.angulo(v1_x, v1_y, v2_x, v2_y)  # Calculo o cos entre v1 e v2 na busca do maior cos, que então será o menor angulo

                if cos < cos_ant:
                    cos_ant = cos
                    maior_x = self.conj_pontos[i][0]  # E então a variável menor fica com o valor do ponto que o loop está olhando
                    maior_y = self.conj_pontos[i][1]


            i = i + 1


        return [maior_x, maior_y]

    def angulo(self, v1_x, v1_y, v2_x, v2_y):
        # Fórmula do Produto interno
        # cos(teta) = c = <v1,v2> / |v1||v2|

        norma_v1 = math.sqrt(v1_x ** 2 + v1_y ** 2)

        norma_v2 = math.sqrt(v2_x ** 2 + v2_y ** 2)

        cos = ((v1_x * v2_x) + (v1_y * v2_y)) / (norma_v1 * norma_v2)

        return cos
