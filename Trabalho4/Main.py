# coding=utf-8

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from Delaunay import Delaunay


# Variáveis Globais
DIMX = 600  # Definindo tamanho da tela na horizontal
DIMY = 600  # Definindo tamanho da tela na vertical

pos_x = 0.0
pos_y = 0.0

conj_pontos = []  # Representa o conjunto de pontos da minha entrada que quero encontrar o Fecho Convexo


def main():
    # Inicializa glut e cria janela
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)  # Determinando o tipo da janela com um buffer duplo
    # e o modelo de representação de cores

    glutInitWindowSize(DIMX, DIMY)  # Tamanho da tela é 600x600
    glutCreateWindow('Trabalho 4 - Larissa Galeno - Delaunay')
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
    global conj_pontos

    key = key.decode("utf-8")
    if str(key) == 'r':  # Apertar a tecla r para dizer ao algoritmo que o usuário acabou de entrar com o conjunto de pontos
        '''
            Nesse caso se o usuário apertar 'r' o programa irá entende que o usuário já entrou com o conjunto de pontos
        '''
        # Se o usuário apertar r devo começar o algorimo da Traingulação

        triangulacao = Delaunay(conj_pontos)
        triangulacao.encontraTriangulo()

    if str(key) == 'b':  # Limpar o canvas
        conj_pontos = []

    glutPostRedisplay()


if __name__ == '__main__':
    main()