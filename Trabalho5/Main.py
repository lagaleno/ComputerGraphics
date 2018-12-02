# coding=utf-8

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy

from CurvaBezier import CurvaBezier


# Variáveis Globais
DIMX = 600  # Definindo tamanho da tela na horizontal
DIMY = 600  # Definindo tamanho da tela na vertical

pos_x = 0.0
pos_y = 0.0

conj_pontos = []  # Representa o conjunto de pontos da minha entrada que quero encontrar o Fecho Convexo
bezier = []

def main():
    # Inicializa glut e cria janela
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)  # Determinando o tipo da janela com um buffer duplo
    # e o modelo de representação de cores

    glutInitWindowSize(DIMX, DIMY)  # Tamanho da tela é 600x600
    glutCreateWindow('Trabalho 5 - Larissa Galeno - Curva de Bezier')
    poligonal()
    glutKeyboardFunc(keyboard)

    glutDisplayFunc(display)
    glutMainLoop()

    return


def display():

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Mudando a cor do fundo para branco
    glClear(GL_COLOR_BUFFER_BIT)  # Carregando a cor do fundo no Buffer


    glPointSize(4.0)
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_LINE_STRIP)

    #Desenhando a poligonal
    for ponto in conj_pontos:
        glVertex3f(ponto[0], ponto[1], ponto[2])

    glEnd()

    glPointSize(4.0)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_STRIP)

    #Desenhando a curva de Bezier
    for ponto_curva in bezier:
        glVertex3f(ponto_curva[0], ponto_curva[1], ponto_curva[2])

    glEnd()

    glFlush()
    glutSwapBuffers()



def keyboard(key, x, y):
    global conj_pontos, bezier

    key = key.decode("utf-8")
    if str(key) == 'r':
        '''
            Nesse caso se o usuário apertar 'r' o programa irá desenhar a curva de Beizer
            
        '''
        curva = CurvaBezier(conj_pontos, bezier)
        bezier = curva.encontra_curva()
        print(bezier)

    if str(key) == 'e': #rotação para cima
        glRotatef(-2.0, 2.0, 0.0, 0.0)

    if str(key) == 's': #rotação para esquerda
        glRotatef(-2.0, 0.0, 2.0, 0.0)

    if str(key) == 'd': #rotação para baixo
        glRotatef(2.0, 2.0, 0.0, 0.0)

    if str(key) == 'f': #rotação pra direita
        glRotatef(2.0, 0.0, 2.0, 0.0)


    glutPostRedisplay()

def poligonal():
    global conj_pontos

    conj_pontos.append([round(random.uniform(-1.0, 1.0)), 0.0, 0.0])

    conj_pontos.append([-0.3, 0.5, -0.5])

    conj_pontos.append([0.0, 0.5, 0.0])

    conj_pontos.append([0.0, -0.5, 0.5])

    conj_pontos.append([0.3, -0.5, 0.5])

    conj_pontos.append([0.5, 0.0, 0.0])


if __name__ == '__main__':
    main()