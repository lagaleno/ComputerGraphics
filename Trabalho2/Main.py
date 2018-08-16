# coding=utf-8

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

# Variáveis Globais
DIMX = 600 #Definindo tamanho da tela na horizontal
DIMY = 600 #Definindo tamanho da tela na vertical

pos_x = 0.0
pos_y = 0.0

acabouPoligono = False #Variável booleana que irá determinar se está no momento do usuário escolher o ponto isolado para o algoritmo analisar se está dentro ou fora
pontos = [] #Representa o ponto que eu quero saber se está dentro ou fora do meu poligono

pontosPoligono = [] #Essa lista no inicio irá guardar os pontos que o usuário escolheu para o poligono

def main():

    # Inicializa glut e cria janela
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)  # Determinando o tipo da janela com um buffer duplo
    # e o modelo de representação de cores

    glutInitWindowSize(DIMX, DIMY)  # Tamanho da tela é 600x600
    glutCreateWindow('Trabalho 2 - Larissa Galeno')
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

    glBegin(GL_LINE_STRIP) #poderia torcar essa linha por glBegin(GL_LINE_LOOP)

    for ponto in pontosPoligono:
        glVertex2f(ponto[0], ponto[1]) #Desenhando as linhas entre os pontos selecionados

    glEnd()

    glPointSize(4.0)
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POINTS) #Para desenhar pontos

    for ponto in pontosPoligono:
        glVertex2f(ponto[0], ponto[1]) #Desenhando os pontos ao clicar na posição


    glEnd()

    #Dando um destaque ao ponto que iremos descobrir se está dentro ou fora do Poligono
    glPointSize(8.0)
    glColor3f(1.0, 0.5, 1.0)
    glBegin(GL_POINTS) #Para desenhar o ponto que o algoritmo irá verificar se está dentro ou fora do Poligono

    '''
        Caso o vetor não esteja vazio, ou seja, caso o meu usuário já tenha terminado de entrar com o poligono e selecionou o ponto que quer saber se está dentro ou fora. 
    '''
    if len(pontos) > 0:
        glVertex2f(pontos[0][0], pontos[0][1]) # Desenho o ponto em questão

    glEnd()


    glFlush()
    glutSwapBuffers()


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        converter(x, y)
        glutPostRedisplay()

def keyboard(key, x, y):
    global pontosPoligono, acabouPoligono, pontos

    key = key.decode("utf-8")
    if str(key) == 'r': #Apertar a tecla r para dizer ao algoritmo que o usuário acabou o poligono e vai entrar com o ponto
        '''
            Nesse caso se o usuário apertar 'r' o programa está juntando o último ponto que o usuário clicou com o primeiro.
            Fechando, assim, o meu poligono. Poderia ter usado GL_LINE_LOOP que o openGL teria fechado automaticamente
        '''
        pontosPoligono.append(pontosPoligono[0])
        acabouPoligono = True

    if str(key) == 'b': #Limpar o canvas
        pontosPoligono = []
        pontos = []

    glutPostRedisplay()


'''
Converte as coordenadas vinda do mouse para o padrão o do OpenGL
'''
def converter(x, y):
    global pos_x, pos_y, pontos, pontosPoligono

    pos_x = 2 * (x / DIMX) - 1  # x é o parâmetro com o a posição em pixels
    pos_y = -(2 * (y / DIMY) - 1)  # y é o parâmetro com a posição em pixels;
    # lembrando que y_pos irá crescer para baixo

    if acabouPoligono is False:
        pontosPoligono.append([pos_x, pos_y])  # No minha lista Pontos vou possuir listar dentro que possuem somente dois elementos
        # representando a pos_x e a pos_y
    else:
        pontos.clear()
        pontos.insert(0, [pos_x, pos_y]) #Adiciono o ponto que eu quero saber se está dentro ou não do Poligono
        print(pontos)









if __name__ == '__main__':
    main()
