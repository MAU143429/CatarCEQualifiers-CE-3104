import pygame
import objects

'''
Se cargan las imagenes de los jugadores
'''


# EQUIPO 1 CAMISAS ROJAS Y NEGRAS

player1_t1 = pygame.image.load("player 1 E1.png")
player2_t1 = pygame.image.load("player 2 E1.png")
player3_t1 = pygame.image.load("player 3 E1.png")
player4_t1 = pygame.image.load("player 4 E1.png")
player5_t1 = pygame.image.load("player 5 E1.png")
player6_t1 = pygame.image.load("player 6 E1.png")
player7_t1 = pygame.image.load("player 7 E1.png")
player8_t1 = pygame.image.load("player 8 E1.png")
player9_t1 = pygame.image.load("player 9 E1.png")
player10_t1 = pygame.image.load("player 10 E1.png")
player11_t1 = pygame.image.load("player 11 E1.png")

# EQUIPO 1 CAMISAS ROJAS Y AZULES

player1_t2 = pygame.image.load("player 1 E2.png")
player2_t2 = pygame.image.load("player 2 E2.png")
player3_t2 = pygame.image.load("player 3 E2.png")
player4_t2 = pygame.image.load("player 4 E2.png")
player5_t2 = pygame.image.load("player 5 E2.png")
player6_t2 = pygame.image.load("player 6 E2.png")
player7_t2 = pygame.image.load("player 7 E2.png")
player8_t2 = pygame.image.load("player 8 E2.png")
player9_t2 = pygame.image.load("player 9 E2.png")
player10_t2 = pygame.image.load("player 10 E2.png")
player11_t2 = pygame.image.load("player 11 E2.png")

'''
Imagen del balon
'''

ball_img = pygame.image.load("balon.png")

'''
Icono y Fondos
'''
bg1 = pygame.image.load("start.png")
icon = pygame.image.load("icon.png")
main_bg = pygame.image.load("bg.png")


'''
Se crean cada uno de los jugadores 
'''
p1_t1 = objects.Player(player1_t1, 0, 0, 0, 0)
p2_t1 = objects.Player(player2_t1, 0, 0, 0, 0)
p3_t1 = objects.Player(player3_t1, 0, 0, 0, 0)
p4_t1 = objects.Player(player4_t1, 0, 0, 0, 0)
p5_t1 = objects.Player(player5_t1, 0, 0, 0, 0)
p6_t1 = objects.Player(player6_t1, 0, 0, 0, 0)
p7_t1 = objects.Player(player7_t1, 0, 0, 0, 0)
p8_t1 = objects.Player(player8_t1, 0, 0, 0, 0)
p9_t1 = objects.Player(player9_t1, 0, 0, 0, 0)
p10_t1 = objects.Player(player10_t1, 0, 0, 0, 0)
p11_t1 = objects.Player(player11_t1, 0, 0, 0, 0)

p1_t2 = objects.Player(player1_t2, 0, 0, 0, 0)
p2_t2 = objects.Player(player2_t2, 0, 0, 0, 0)
p3_t2 = objects.Player(player3_t2, 0, 0, 0, 0)
p4_t2 = objects.Player(player4_t2, 0, 0, 0, 0)
p5_t2 = objects.Player(player5_t2, 0, 0, 0, 0)
p6_t2 = objects.Player(player6_t2, 0, 0, 0, 0)
p7_t2 = objects.Player(player7_t2, 0, 0, 0, 0)
p8_t2 = objects.Player(player8_t2, 0, 0, 0, 0)
p9_t2 = objects.Player(player9_t2, 0, 0, 0, 0)
p10_t2 = objects.Player(player10_t2, 0, 0, 0, 0)
p11_t2 = objects.Player(player11_t2, 0, 0, 0, 0)

ball = objects.Ball(ball_img,13)


'''
Listas de equipo
'''
team_1 = [p1_t1,p2_t1,p3_t1,p4_t1,p5_t1,p6_t1,p7_t1,p8_t1,p9_t1,p10_t1,p11_t1]
team_2 = [p1_t2,p2_t2,p3_t2,p4_t2,p5_t2,p6_t2,p7_t2,p8_t2,p9_t2,p10_t2,p11_t2]
