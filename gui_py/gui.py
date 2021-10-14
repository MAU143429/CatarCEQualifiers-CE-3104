import pygame
import players
import keyboard
import game


'''
Esta clase permite crear una gui inicial.
'''
class gui():

    '''
    Inicializa la interfaz
    '''
    def init_gui(self):

        '''
        Se inicializa el pygame
        '''

        pygame.init()

        '''
        Creamos la ventana de juego 
        '''
        window_width= 700
        window_height= 500
        window = pygame.display.set_mode((window_height,window_width))

        '''
        Cargamos recursos como imagenes de fondo e iconos
        '''

        black = (0, 0, 0)
        pygame.display.set_caption("Catar-CE-Qualifiers")
        pygame.display.set_icon(players.icon)
        font = pygame.font.Font('freesansbold.ttf', 14)
        text = font.render('Press SPACE to start the game!', True, black)
        textRect = text.get_rect()
        textRect.center = (window_height // 2, window_width // 2)
        running = True

        '''
        Ciclo principal de la interfaz inicial
        '''
        while running:

            '''
            Espera cualquier evento por parte del usuario (cerrar ventana o iniciar partida)
            '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if keyboard.is_pressed('space'):
                    g_start = game.game()
                    g_start.start_game()


            window.blit(players.bg1, (0, 0))
            window.blit(text, (150 , 10))
            pygame.display.flip()






