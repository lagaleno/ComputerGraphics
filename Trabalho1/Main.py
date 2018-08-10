
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

#Variáveis Globais
DIMX = 600
DIMY = 600

pos_x = 0.0
pos_y = 0.0


def main():
    # Inicializa glut e cria janela
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA) #Determinando o tipo da janela com um buffer duplo
                                                 # e o modelo de representação de cores
    glutInitWindowSize(DIMX, DIMY) #Tamanho da tela é 600x600
    glutCreateWindow('Trabalho 1 - Larissa Galeno')
    gluOrtho2D(0, DIMX-1, DIMY-1, 0)

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
    glVertex2f(pos_x, pos_y)

    glEnd()

    glFlush()
    glutSwapBuffers()

def mouse(button, state, x, y):

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        converte(x, y)
        glutPostRedisplay()

def converte(x, y):
    global x_pos, y_pos

    x_pos = 2*(x/600) - 1 # x é o parâmetro com o a posição em pixels
    y_pos = 2*(y/600) - 1

    print(x_pos)
    print(y_pos)



if __name__ == '__main__':
    main()