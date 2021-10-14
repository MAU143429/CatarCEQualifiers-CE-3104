import sys
import pygame
import players as players
from threading import *
import board

team_1_structure = 0
team_2_structure = 0

'''
Esta clase es la del juego principal, en ella se aloja el ciclo principal de juego y las acciones principales
'''
class game():

    global team_1_structure
    global team_2_structure

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

        if team_1_structure == 0 and team_2_structure == 0:
            print("ERROR AL INICIAR EL JUEGO, NO SE HAN AGREGADO LAS ALINEACIONES. SALIENDO.....")
            sys.exit()
        else:
            print("EL PARTIDO COMENZARA PRONTO.... ALINEACION DEL EQUIPO 1 --> " + str(team_1_structure) + " ALINEACION DEL EQUIPO 2 --> " + str(team_2_structure))

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
        #table.print_boxes()
        #table.print_posx()
        #table.print_posy()

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

            #EQUIPO 1
            window1.blit(players.player1_t1, (0 , 250))
            window1.blit(players.player2_t1, (100 , 100))
            window1.blit(players.player3_t1, (150 , 200))
            window1.blit(players.player4_t1, (150 , 350))
            window1.blit(players.player5_t1, (100 , 450))
            window1.blit(players.player6_t1, (300 , 100))
            window1.blit(players.player7_t1, (400 , 200))
            window1.blit(players.player8_t1, (400 , 350))
            window1.blit(players.player9_t1, (300 , 450))
            window1.blit(players.player10_t1, (550 , 200))
            window1.blit(players.player11_t1, (550 , 350))

            #E

            window1.blit(players.player1_t2, (1150 , 250))
            window1.blit(players.player2_t2, (1100 , 100))
            window1.blit(players.player3_t2, (1100 , 450))
            window1.blit(players.player4_t2, (1050 , 200))
            window1.blit(players.player5_t2, (1050 , 350))
            window1.blit(players.player6_t2, (900 , 400))
            window1.blit(players.player7_t2, (900 , 250))
            window1.blit(players.player8_t2, (900 , 100))
            window1.blit(players.player9_t2, (700 , 100))
            window1.blit(players.player10_t2, (700 , 250))
            window1.blit(players.player11_t2, (700 , 400))


            # BALON
            window1.blit(players.ball, (600 , 250))
            pygame.display.flip()


