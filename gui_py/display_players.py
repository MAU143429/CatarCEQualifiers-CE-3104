import time

import players
import game

team_1_structure = []
team_2_structure = []


class display_players():

    global team_1_structure
    global team_2_structure

    '''
    Algoritmo que lee las formaciones y coloca a los jugadores segun corresponda, a su vez asigna valores
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


    '''
    Este metodo se encarga de consultar posiciones para refrescar las imagenes en la ventana
    '''
    def update(self, window1):

        for player in players.team_1:
            # Revisa si a ocurrido algun gol.
            if self.isGoal(144):
                game.score1 += 1

            #Verifica si algun jugador tiene la bola
            if player.getBox() == players.ball.getBox():
                route = self.hit_distance(player,1)
                for box in route:
                    players.ball.setBox(box)
                    window1.blit(players.ball_img, (players.ball.getPosX() ,players.ball.getPosY()))
                    time.sleep(0.250)

             # Actualiza el frame de cada jugador
            window1.blit(player.image,(player.getPosX(),player.getPosY()))

            #print( "TEAM 1 " +str(player.position) + " " + str(player.box) + " en la casilla con posiciones --> x : " + str(player.getPosX()) + " y: " + str(player.getPosY()))


        for player2 in players.team_2:
            # Revisa si a ocurrido algun gol.
            if self.isGoal(121):
                game.score2 += 1
            #Verifica si algun jugador tiene la bola
            if player2.getBox() == players.ball.getBox():
                route = self.hit_distance(player2,2)
                for box in route:
                    players.ball.setBox(box)
                    window1.blit(players.ball_img, (players.ball.getPosX() ,players.ball.getPosY()))
                    time.sleep(0.250)
            # Actualiza el frame de cada jugador
            window1.blit(player2.image,(player2.getPosX(),player2.getPosY()))

            #print("TEAM 2 " + str(player2.position) + " " + str(player2.box)+ " en la casilla con posiciones --> x : " + str(player2.getPosX()) + " y: " + str(player2.getPosY()))


        window1.blit(players.ball_img, (players.ball.getPosX() ,players.ball.getPosY()))

    def isGoal(self,box):

        if players.ball.getBox() == box:
            return True
        else:return False

    def hit_distance(self,player,team):
        hit_route = []
        steps = 0
        if team == 1:
            path = self.create_move(player.getBox(),144)
            while len(hit_route) < player.getForce():
                hit_route.append(path[steps])
                steps += 1
        else:
            path = self.create_move(player.getBox(),121)
            while len(hit_route) < player.getForce():
                hit_route.append(path[steps])
                steps += 1
        return hit_route

    def init_movements(self):

        for player in players.team_1:
            new_list = self.create_move(player.getBox(),players.ball.getBox())
            final_list = self.verify_path(new_list,player.getPos(),player.getDistance(),1)
            player.setMovements(final_list)

        for player2 in players.team_2:
            new_list = self.create_move(player2.getBox(),players.ball.getBox())
            final_list = self.verify_path(new_list,player2.getPos(),player2.getDistance(),2)
            player2.setMovements(final_list)


    def verify_path(self,path,player_pos,max_movs,team):
        new_path = []
        cont = 0
        stop = False

        if player_pos == 3 and team == 1:
            while not stop or (cont < len(path)):
                if len(new_path) < int(max_movs):
                    c_row = self.getRow(path[cont])
                    c_col = self.getCol(path[cont])
                    if c_col <= 1:
                        if c_row >= 4 or c_row <= 6:
                            new_path.append(path[cont])
                    else: stop = True
                cont += 1
            stop = False
            return new_path

        if player_pos == 3 and team == 2:
            while not stop or (cont < len(path)):
                if len(new_path) < max_movs:
                    c_row = self.getRow(path[cont])
                    c_col = self.getCol(path[cont])
                    if c_col >= 23:
                        if c_row >= 4 or c_row <= 6:
                            new_path.append(path[cont])
                    else: stop = True
                cont += 1
            stop = False
            return new_path

        #ES UN DEFENSA
        if player_pos == 0:
            while not stop or (cont < len(path)):
                if len(new_path) < int(max_movs):
                    c_col = self.getCol(path[cont])
                    if c_col <= 8:
                        new_path.append(path[cont])
                    else: stop = True
                cont += 1
            stop = False
            return new_path

        # ES UN MEDIO
        if player_pos == 1:
            while not stop or (cont < len(path)):
                if len(new_path) < int(max_movs):
                    c_col = self.getCol(path[cont])
                    if c_col >= 8:
                        new_path.append(path[cont])
                    else: stop = True
                cont += 1
            stop = False
            return new_path

        # ES UN DELANTERO

        if player_pos == 2:
            while not stop or (cont < len(path)):
                if len(new_path) < int(max_movs):
                    c_col = self.getCol(path[cont])
                    if c_col >= 16:
                        new_path.append(path[cont])
                    else: stop = True
                cont += 1
            stop = False
            return new_path


    def getRow(self,box1):

        row = box1 // 24
        if box1 % 24 == 0:
            row -= 1
        return row

    def getCol(self,box1):

        col = 24
        if box1 % 24 != 0:
            col = (box1 % 24)-1
        return col


    def create_move(self,current_box,ball_box):
        result = []
        c_row = self.getRow(current_box)
        ball_row = self.getRow(ball_box)
        c_column = self.getCol(current_box)
        ball_column = self.getCol(ball_box)
        road_x = c_column - ball_column
        road_y = c_row - ball_row
        movs = 0
        while road_x != 0 or road_y != 0:
          # Movimiento par se mueve x
          if movs % 10 % 2 == 0:
              if road_x != 0:
                  if road_x > 0 :
                      result.append(current_box - 1)
                      current_box -= 1
                      road_x -= 1
                  else:
                      result.append(current_box + 1)
                      current_box += 1
                      road_x += 1
              movs += 1
          # Movimiento par se mueve y
          else:
              if road_y != 0:
                  if road_y > 0:
                      result.append(current_box - 24)
                      current_box -= 24
                      road_y -= 1
                  else:
                      result.append(current_box + 24)
                      current_box += 24
                      road_y += 1
              movs += 1
        return result

















