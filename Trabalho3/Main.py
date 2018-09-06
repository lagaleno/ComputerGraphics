# coding=utf-8

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys

# Variáveis Globais
DIMX = 600 #Definindo tamanho da tela na horizontal
DIMY = 600 #Definindo tamanho da tela na vertical

pos_x = 0.0
pos_y = 0.0

conj_pontos = [] #Representa o conjunto de pontos da minha entrada que quero encontrar o Fecho Convexo

pontos = [] #Lista de pontos do meu fecho convexo

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
    glBegin(GL_POINTS) #Para desenhar pontos

    for ponto in conj_pontos:
        glVertex2f(ponto[0], ponto[1]) #Desenhando os pontos ao clicar na posição

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
    # lembrando que y_pos irá crescer para baixo

    conj_pontos.append([pos_x, pos_y])

def keyboard(key, x, y):

    key = key.decode("utf-8")
    if str(key) == 'r': #Apertar a tecla r para dizer ao algoritmo que o usuário acabou de entrar com o conjunto de pontos
        '''
            Nesse caso se o usuário apertar 'r' o programa irá entende que o usuário já entrou com o conjunto de pontos
        '''
        jarvis()

    if str(key) == 'b': #Limpar o canvas
        pass

    glutPostRedisplay()


def jarvis():

    global pontos

    #p0 representa o ponto inicial de menor coordenada y
    conj_pontos.sort(key=lambda k: k[1]) #Ordeando de maneira crescente a lisa de entrada deconjunto depontos
    pontos.append(conj_pontos[0]) #Com isso p0 terá o vértice com o menor y! Que está na primeira posição do conj_pontos
    pontos.append(proximo(pontos[0], [1, 0])) #pegando o p2

    print(pontos)
    i = 1

    while pontos[i] != pontos[0]:

        pontos[i].append(proximo(pontos[i-1], ))
        i = i+1


'''
    O retorno da função é o ponto que possui a menor angulação com o vetor.
'''
def proximo(ponto, vetor):

    menor = [] #A variavel menor irá guardar o ponto que possui a angulação menor
    cos_ant = -2

    #Retorna um ponto p tal que o angulo de v e p0p seja minimo

    menor = ponto

    for p in conj_pontos:
        cos = angulo(vetor, )

        if cos > cos_ant:
            #muda menor
            pass

'''
    Para calcular o angulo, iremos usar o Produto interno para achar o cos(teta);
    O angulo que tiver o maior cos(teta) será o próximo ponto, pois terá a angulação menor.
    
    Sendo v2 o vetor entre os dois pontos

    O retorno da função é cos(teta) entre o vetor que sai do ponto e o vetor que liga os pontos.
'''
def angulo(v1, v2):

    #Fórmula do Produto interno
    # cos(teta) = c = <v1,v2> / |v1||v2|

    norma_v1 = math.sqrt(v1[0]**2 + v1[1]**2)

    norma_v2 = math.sqrt(v2[0]**2 + v2[1]**2)

    cos = ((v1[0] * v2[0]) + (v1[1] * v2[1]))/(norma_v1 * norma_v2)

    print(cos)

    return cos


if __name__ == '__main__':
    main()
