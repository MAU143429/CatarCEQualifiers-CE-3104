import sys
import pygame
import players as players
import display_players
from threading import *
import board

teams = []


'''
Esta clase es la del juego principal, en ella se aloja el ciclo principal de juego y las acciones principales
'''
class game():

    '''
    Metodo que llama a la interfaz de juego
    '''
    def start_game(self):
        thread1 = Thread(target=self.init_game(), args=())
        thread1.start()
        thread1.join()

    '''
    Juego principal, aqui suceden la mayoria de eventos, desde la creacion de la interfaz, posicionamiento de alineaciones entre otras
    funciones principales
    '''
    def init_game(self):

        '''
        Consulta sobre la existencia de las alineaciones, caso contrario cierra el juego debido a la falta de ese parametro
        :return: sys.exit() cierra el juego por completo.
        '''

        if len(display_players.team_1_structure) == 0 and len(display_players.team_2_structure) == 0:
            print("ERROR AL INICIAR EL JUEGO, NO SE HAN AGREGADO LAS ALINEACIONES. SALIENDO.....")
            sys.exit()
        else:
            print("EL PARTIDO COMENZARA PRONTO.... ALINEACION DEL EQUIPO 1 --> " + str(display_players.team_1_structure) + " ALINEACION DEL EQUIPO 2 --> " + str(display_players.team_2_structure))

        '''
        Aspectos operativos de la ventana como nombre dimensiones y se cargan imagenes de icono y fondo
        '''
        window1_width=600
        window1_height=1200
        window1 = pygame.display.set_mode((window1_height,window1_width))
        pygame.display.set_caption("Catar-CE-Qualifiers")
        pygame.display.set_icon(players.icon)

        '''
        Se crea una matriz de objetos de tipo casilla, los usados para cada movimiento y animacion.
        '''
        table = board.board()
        table.create_board()
        display_players.display_players().display(window1)




        '''
        Ciclo principal de juego
        '''
        running = True
        while running:

            '''
            Detecta eventos de interfaz como que el juego sea cerrado
            '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            window1.blit(players.main_bg, (0, 0))

            update = display_players.display_players()
            update.update(window1)

            pygame.display.flip()


