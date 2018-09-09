# coding=utf-8

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys

# Variáveis Globais
DIMX = 600  # Definindo tamanho da tela na horizontal
DIMY = 600  # Definindo tamanho da tela na vertical

pos_x = 0.0
pos_y = 0.0

conj_pontos = []  # Representa o conjunto de pontos da minha entrada que quero encontrar o Fecho Convexo
pontos = []  # Lista de pontos do meu fecho convexo


def main():
    # Inicializa glut e cria janela
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)  # Determinando o tipo da janela com um buffer duplo
    # e o modelo de representação de cores

    glutInitWindowSize(DIMX, DIMY)  # Tamanho da tela é 600x600
    glutCreateWindow('Trabalho 3 - Larissa Galeno - Jarvis')
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)

    glutDisplayFunc(display)
    glutMainLoop()

    return

def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Mudando a cor do fundo para branco
    glClear(GL_COLOR_BUFFER_BIT)  # Carregando a cor do fundo no Buffer

    glPointSize(4.0)
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POINTS)  # Para desenhar pontos

    for ponto in conj_pontos:
        glVertex2f(ponto[0], ponto[1])  # Desenhando os pontos ao clicar na posição

    glEnd()

    glPointSize(4.0)
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_LINE_STRIP)

    for ponto in pontos:
        glVertex2f(ponto[0], ponto[1])  # Desenhando as linhas entre os pontos do Fecho Convexo

    glEnd()

    glFlush()
    glutSwapBuffers()


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        converter(x, y)
        glutPostRedisplay()


'''
Converte as coordenadas vinda do mouse para o padrão o do OpenGL
'''
def converter(x, y):
    global pos_x, pos_y, conj_pontos

    pos_x = 2 * (x / DIMX) - 1  # x é o parâmetro com o a posição em pixels
    pos_y = -(2 * (y / DIMY) - 1)  # y é o parâmetro com a posição em pixels;
    # lembrando que pos_y irá crescer para baixo

    conj_pontos.append([pos_x, pos_y]) #Adicionando a minha lista de entrada os pontos com as coordenadas certas


def keyboard(key, x, y):
    global conj_pontos, pontos

    key = key.decode("utf-8")
    if str(key) == 'r':  # Apertar a tecla r para dizer ao algoritmo que o usuário acabou de entrar com o conjunto de pontos
        '''
            Nesse caso se o usuário apertar 'r' o programa irá entende que o usuário já entrou com o conjunto de pontos
        '''
        jarvis()

    if str(key) == 'b':  # Limpar o canvas
        conj_pontos = []
        pontos = []

    glutPostRedisplay()


def jarvis():
    global pontos

    conj_pontos.sort(key=lambda k: k[1])  # Ordeando de maneira crescente a lisa de entrada deconjunto depontos
    pontos.append(conj_pontos[0]) #acho o p0 que representa o ponto inicial de menor coordenada y
    #acho o próximo ponto do meu fecho convexo;
    pontos.append(proximo(pontos[0], 1, 0)) #Sendo que estou passando o vetor [1, 0] que o vetor que sai do meu p0


    i = 1
    # Enquanto o próximo for diferente do primeiro, eu rodo o loop
    while pontos[i] != pontos[0]:

        # Achando o vetor que está entre o ponto que estou analisando e o candidato a próximo
        v1_x = pontos[i][0] - pontos[i-1][0] #coordenada x
        v1_y = pontos[i][1] - pontos[i-1][1] #coordenada y

        pontos.append(proximo(pontos[i], v1_x, v1_y)) #Assim analiso se o ponto é realmente válido para ser o próximo, se for adiciono a minha lista do fecho convexo
        i = i+1


'''
    O retorno da função é o ponto que possui a menor angulação com o vetor.
'''
def proximo(ponto, v1_x, v1_y):
    # A variavel menor irá guardar o ponto que possui a angulação menor; Inicializada com -2, pois qualquer angulo será maior que esse
    cos_ant = -2

    #Varáve irá guarda as coordenadas do ponto que possui o menor angulo entre os vetores
    menor_x = 0 #Coordanada x
    menor_y = 0 #Coordenada y


    # Retorna um ponto p tal que o angulo de v1 e v2 (p0p) seja minimo
    i = 0
    while i < len(conj_pontos):

        # Se o ponto que estou analisando é o mesmo ponto que o loop está, não tem necessidade de fazer a conta, pois ele com certeza não será
        if ponto == conj_pontos[i]:
            pass

        #Caso seja diferente eu efetivamente faço a conta
        else:
            # Calculo o vetor entre o ponto que estou analisando com os outros pontos para analisar o angulo
            v2_x = conj_pontos[i][0] - ponto[0] #coordenada x
            v2_y = conj_pontos[i][1] - ponto[1] #coordenada y

            cos = angulo(v1_x, v1_y, v2_x, v2_y) #Calculo o cos entre v1 e v2 na busca do maior cos, que então será o menor angulo

            if cos > cos_ant: #Se o retorno qe eu tive for maior que o anterior significa que eu encontrei um ponto mais qualificado para o meu fecho convexo
                cos_ant = cos # Se é mais qualificado eu troco
                menor_x = conj_pontos[i][0] #E então a variável menor fica com o valor do ponto que o loop está olhando
                menor_y = conj_pontos[i][1]

        i = i+1

    # Retorno em formato de lista para adicionar a minha lista de pontos
    return [menor_x, menor_y]


'''
    Para calcular o angulo, iremos usar o Produto interno para achar o cos(teta);
    O angulo que tiver o maior cos(teta) será o próximo ponto, pois terá a angulação menor.

    Sendo v2 o vetor entre os dois pontos

    O retorno da função é cos(teta) entre o vetor que sai do ponto e o vetor que liga os pontos.
'''
def angulo(v1_x, v1_y, v2_x, v2_y):
    # Fórmula do Produto interno
    # cos(teta) = c = <v1,v2> / |v1||v2|

    norma_v1 = math.sqrt(v1_x ** 2 + v1_y ** 2)

    norma_v2 = math.sqrt(v2_x ** 2 + v2_y ** 2)

    cos = ((v1_x * v2_x) + (v1_y * v2_y)) / (norma_v1 * norma_v2)

    return cos


if __name__ == '__main__':
    main()