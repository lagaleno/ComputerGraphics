
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

#Variáveis Globais
DIMX = 600
DIMY = 600

pos_x = 0.0
pos_y = 0.0

pontos = []


def main():
    # Inicializa glut e cria janela
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA) #Determinando o tipo da janela com um buffer duplo
                                                 # e o modelo de representação de cores

    glutInitWindowSize(DIMX, DIMY) #Tamanho da tela é 600x600
    glutCreateWindow('Trabalho 1 - Larissa Galeno')
    glutMouseFunc(mouse)


    glutDisplayFunc(display)
    glutMainLoop()

    return


def display():
    glClearColor(1.0, 1.0, 1.0, 1.0) #Mudando a cor do fundo para branco
    glClear(GL_COLOR_BUFFER_BIT) #Carregando a cor do fundo no Buffer

    glColor3f(1.0, 0.0, 1.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)

    for ponto in pontos:
        glVertex2f(ponto[0], ponto[1])

    glEnd()

    glFlush()
    glutSwapBuffers()

def mouse(button, state, x, y):

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        converte(x, y)
        glutPostRedisplay()

def converte(x, y):
    global pos_x, pos_y

    pos_x = 2*(x/DIMX) - 1 # x é o parâmetro com o a posição em pixels
    pos_y = -(2*(y/DIMY) - 1) # y é o parâmetro com a posição em pixels;
                           # lembrando que y_pos irá crescer para baixo

    pontos.append([pos_x, pos_y]) # No minha lista Pontos vou possuir listar dentro que possuem somente dois elementos
                                  # representando a pos_x e a pos_y

    print(pontos)

    print(pos_x)
    print(pos_y)



if __name__ == '__main__':
    main()