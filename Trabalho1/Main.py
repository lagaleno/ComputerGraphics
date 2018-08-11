# coding=utf-8

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

# Variáveis Globais
DIMX = 600
DIMY = 600

pos_x = 0.0
pos_y = 0.0

pontos = []
dist = []
novosPontos = []

def main():
    # Inicializa glut e cria janela
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)  # Determinando o tipo da janela com um buffer duplo
    # e o modelo de representação de cores

    glutInitWindowSize(DIMX, DIMY)  # Tamanho da tela é 600x600
    glutCreateWindow('Trabalho 1 - Larissa Galeno')
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)

    glutDisplayFunc(display)
    glutMainLoop()

    return


def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Mudando a cor do fundo para branco
    glClear(GL_COLOR_BUFFER_BIT)  # Carregando a cor do fundo no Buffer

    glColor3f(1.0, 0.0, 1.0)
    glPointSize(10.0)
    glBegin(GL_LINE_STRIP)

    for ponto in pontos:
        glVertex2f(ponto[0], ponto[1])

    glEnd()

    glFlush()
    glutSwapBuffers()


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        converte(x, y)
        glutPostRedisplay()


def keyboard(key, x, y):
    key = key.decode("utf-8")
    if str(key) == 'r':
        suaviza()


def converte(x, y):
    global pos_x, pos_y

    pos_x = 2 * (x / DIMX) - 1  # x é o parâmetro com o a posição em pixels
    pos_y = -(2 * (y / DIMY) - 1)  # y é o parâmetro com a posição em pixels;
    # lembrando que y_pos irá crescer para baixo

    pontos.append([pos_x, pos_y])  # No minha lista Pontos vou possuir listar dentro que possuem somente dois elementos
    # representando a pos_x e a pos_y

    # print(pontos)

    # print(pos_x)
    # print(pos_y)


def distancia(ponto):
    # Caso eu esteja olhando o último ponto não existe uma linha para calcular a distancia
    if (ponto + 1) != len(pontos):
        # Fórmula da distancia entre dois pontos => dist = a^2 + b^2
        a = pontos[ponto][0] - pontos[ponto][1]
        b = pontos[ponto + 1][0] - pontos[ponto + 1][1]

        r = (a ** 2 + b ** 2) ** (1 / 2)

        return r


def pontoMedio(ponto):

    if (ponto+1) != len(pontos):

        #Ponto do Meio
        xMedio = (pontos[ponto][0] + pontos[ponto+1][0])/2
        yMedio = (pontos[ponto][1] + pontos[ponto+1][1])/2

        #Entre o Primeiro Ponto e o do Meio
        x1 = (xMedio + pontos[ponto][0])/2
        y1 = (yMedio + pontos[ponto][1])/2

        #Entre o do Meio e o segundo ponto
        x2 = (xMedio + pontos[ponto+1][0])/2
        y2 = (yMedio + pontos[ponto+1][1])/2

        novosPontos.append([x1, y1])
        novosPontos.append([xMedio, yMedio])
        novosPontos.append([x2, y2])


def suaviza():
    novosPontos.append(pontos[0])

    for index, ponto in enumerate(pontos):
        pontoMedio(index)

    novosPontos.append(pontos[-1])

    print(pontos)
    print(novosPontos)


if __name__ == '__main__':
    main()
