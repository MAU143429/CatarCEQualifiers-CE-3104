import  board
import players

team_1_structure = []
team_2_structure = []


class display_players():

    global team_1_structure
    global team_2_structure

    '''
    Algoritmo que lee las formaciones y coloca a los jugadores segun corresponda
    '''
    def display(self, window1):

        # Conjunto de columnas en donde se inicia el spawn de cada grupo de posiciones en su respectivo equipo

        team1_position1 = 4
        team1_position2 = 11
        team1_position3 = 18

        team2_position1 = 21
        team2_position2 = 14
        team2_position3 = 7

        cont = 0
        spawn = 1
        while cont < len(team_1_structure):
            if team_1_structure[cont] % 10 % 2 == 0:
                pivot = ((12-(team_1_structure[cont]))//2)
            else:
                pivot = ((12-(team_1_structure[cont]))//2)+1
            cont2 = 0
            while cont2 < team_1_structure[cont]:
                print("SPAWNEANDO AL JUGADOR --> " + str(spawn))
                if cont == 0:
                    box = (pivot * 24) + team1_position1
                    print("SOY EL BOX DEFENSIVO --> " + str(box))
                    players.team_1[spawn].setBox(box)
                    players.team_1[spawn].setPos(cont)

                if cont == 1:
                    box = (pivot * 24) + team1_position2
                    print("SOY EL BOX MEDIO --> " + str(box))
                    players.team_1[spawn].setBox(box)
                    players.team_1[spawn].setPos(cont)

                if cont == 2:
                    box = (pivot * 24) + team1_position3
                    print("SOY EL BOX DELANTERO --> " + str(box))
                    players.team_1[spawn].setBox(box)
                    players.team_1[spawn].setPos(cont)
                print(str(cont2) + str(spawn)  + str(cont))

                cont2 += 1
                pivot += 1
                spawn += 1
            cont += 1

        cont = 0
        spawn = 1

        while cont < len(team_2_structure):
            if team_2_structure[cont] % 10 % 2 == 0:
                pivot = ((12-(team_2_structure[cont]))//2)
            else:
                pivot = ((12-(team_2_structure[cont]))//2)+1
            cont2 = 0
            while cont2 < team_2_structure[cont]:
                print("SPAWNEANDO AL JUGADOR --> " + str(spawn))
                if cont == 0:
                    box = (pivot * 24) + team2_position1
                    print("SOY EL BOX DEFENSIVO --> " + str(box))
                    players.team_2[spawn].setBox(box)
                    players.team_2[spawn].setPos(cont)

                if cont == 1:
                    box = (pivot * 24) + team2_position2
                    print("SOY EL BOX MEDIO --> " + str(box))
                    players.team_2[spawn].setBox(box)
                    players.team_2[spawn].setPos(cont)

                if cont == 2:
                    box = (pivot * 24) + team2_position3
                    print("SOY EL BOX DELANTERO --> " + str(box))
                    players.team_2[spawn].setBox(box)
                    players.team_2[spawn].setPos(cont)
                print(str(cont2) + str(spawn)  + str(cont))

                cont2 += 1
                pivot += 1
                spawn += 1
            cont += 1



        # Spawn de la bola y los porteros

        # Portero equipo 1
        players.team_1[0].setBox(121)
        players.team_1[0].setPos(3)

        # Portero equipo 2
        players.team_2[0].setBox(144)
        players.team_2[0].setPos(3)

        players.ball.setBox(132)


    def update(self, window1):

        for player in players.team_1:
            print( "TEAM 1 " +str(player.position) + " " + str(player.box) + " en la casilla con posiciones --> x : " + str(player.getPosX()) + " y: " + str(player.getPosY()))
            window1.blit(player.image,(player.getPosX(),player.getPosY()))

        for player2 in players.team_2:
            print("TEAM 2 " + str(player2.position) + " " + str(player2.box)+ " en la casilla con posiciones --> x : " + str(player2.getPosX()) + " y: " + str(player2.getPosY()))
            window1.blit(player2.image,(player2.getPosX(),player2.getPosY()))

        window1.blit(players.ball_img, (players.ball.getPosX() ,players.ball.getPosY()))









