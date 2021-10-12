import pygame
import players as players
import player
import board

'''
Se inicializa el pygame
'''
pygame.init()

'''
Creamos la ventana de juego 
'''
window_width=600
window_height=1200
window = pygame.display.set_mode((window_height,window_width))

pygame.display.set_caption("Catar-CE-Qualifiers")
icon = pygame.image.load("balon.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("bg.png")

table = board.board()
table.create_board()
table.print_boxes()
table.print_posx()
table.print_posy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(bg, (0, 0))

    #EQUIPO 1
    window.blit(players.player1_t1, (0 , 250))
    window.blit(players.player2_t1, (100 , 100))
    window.blit(players.player3_t1, (150 , 200))
    window.blit(players.player4_t1, (150 , 350))
    window.blit(players.player5_t1, (100 , 450))
    window.blit(players.player6_t1, (300 , 100))
    window.blit(players.player7_t1, (400 , 200))
    window.blit(players.player8_t1, (400 , 350))
    window.blit(players.player9_t1, (300 , 450))
    window.blit(players.player10_t1, (550 , 200))
    window.blit(players.player11_t1, (550 , 350))

    #Formacion

    window.blit(players.player1_t2, (1150 , 250))
    window.blit(players.player2_t2, (1100 , 100))
    window.blit(players.player3_t2, (1100 , 450))
    window.blit(players.player4_t2, (1050 , 200))
    window.blit(players.player5_t2, (1050 , 350))
    window.blit(players.player6_t2, (900 , 400))
    window.blit(players.player7_t2, (900 , 250))
    window.blit(players.player8_t2, (900 , 100))
    window.blit(players.player9_t2, (700 , 100))
    window.blit(players.player10_t2, (700 , 250))
    window.blit(players.player11_t2, (700 , 400))


    # BALON
    window.blit(players.ball, (600 , 250))
    pygame.display.flip()







