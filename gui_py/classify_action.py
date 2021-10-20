import display_players
import players as teams
import game

'''
Esta clase contiene metodos que ayudan a traducir los mensajes que llegan del socket
'''
class classify_action():

    '''
    Este metodo permite traducir la linea que recibe a traves del socket
    '''
    def translate_sms(self, sms):
        result = []
        msg = sms.replace(" ", "")
        msg = msg.replace("(" ,"")
        msg = msg.replace(")", ",")
        sms_len = 0
        buffer = ""
        # EL MENSAJE RECIBIDO CORRESPONDE A LAS PARAMETROS DE INICIO DE JUEGO.
        print(msg)
        if msg[0:5] == "START":
            line = msg[5:-1]
            while sms_len < len(line):
                if line[sms_len] != "/" and line[sms_len] != ",":
                    if line[sms_len + 1] != "/" and line[sms_len + 1] != ",":
                        buffer += line[sms_len]
                        buffer += line[sms_len + 1]
                        if len(display_players.team_1_structure) == 3:
                            display_players.team_2_structure.append(int(buffer))
                            buffer = ""
                            sms_len += 1
                        else:
                            display_players.team_1_structure.append(int(buffer))
                            buffer = ""
                            sms_len += 1
                    else:
                        buffer += line[sms_len]
                        if len(display_players.team_1_structure) == 3:
                            display_players.team_2_structure.append(int(buffer))
                            buffer = ""

                        else:
                            display_players.team_1_structure.append(int(buffer))
                            buffer = ""
                sms_len += 1

            print(display_players.team_1_structure)
            print(display_players.team_2_structure)
            return "INIT"

        else:
            print(msg)
            # EL MENSAJE RECIBIDO CORRESPONDE A UNA GENERACION.
            msg = msg.replace("\n", ",")
            char = False
            while(sms_len < len(msg)):
                if msg[sms_len] == ',':
                    if msg[sms_len+1] == ',':
                        break
                    sms_len += 1
                    char = True
                    pass
                if msg[sms_len] == '/' and not char:
                    result.append("T2")
                    sms_len += 1
                    char = True
                if not char:
                    if type(int(msg[sms_len])) == int and msg[sms_len+1] == ',':
                        buffer += msg[sms_len]
                        result.append(buffer)
                        buffer = ""
                        sms_len += 2

                    elif type(int(msg[sms_len])) == int:
                        buffer += msg[sms_len]
                        sms_len += 1
                char = False
            return result

    '''
    Este metodo procesa las instrucciones de generaciones entrantes, luego de que estas fueron traducidas.
    '''
    def recv_sms(self, gen):
        cont = 0
        current = 0
        team_pos = 0
        distance_pos = 2
        force_pos = 3
        if len(gen) != 0:
            print("Aplicando nueva generacion de individuos")
            while cont < len(gen):
                if gen[cont] == "T2":
                    current = 0

                if gen[cont][team_pos] == "1":
                    if len(gen[cont]) == 4:
                        teams.team_1[current].setDistance(gen[current][distance_pos])
                        teams.team_1[current].setForce(gen[current][force_pos])
                    else:
                        teams.team_1[current].setDistance(gen[current][distance_pos + 1])
                        teams.team_1[current].setForce(gen[current][force_pos + 1])

                    current += 1

                if gen[cont][team_pos] == "2":
                    if len(gen[cont]) == 4:
                        teams.team_2[current].setDistance(gen[cont][distance_pos])
                        teams.team_2[current].setForce(gen[cont][force_pos])

                    else:
                        teams.team_2[current].setDistance(gen[cont][distance_pos + 1])
                        teams.team_2[current].setForce(gen[cont][force_pos + 1])
                    current += 1
                cont += 1

            # Se ejecuta el algoritmo de movimiento

            start = display_players.display_players()
            start.init_movements()
            game.move = True









