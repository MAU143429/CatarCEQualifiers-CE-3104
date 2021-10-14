import game

'''
Esta clase contiene metodos que ayudan a traducir los mensajes que llegan del socket
'''
class classify_action():

    '''
    Este metodo permite traducir la linea que recibe a traves del socket
    '''
    def translate_sms(self, sms):
        msg = sms.replace(" ", "")
        msg = msg.replace("(" ,"")
        msg = msg.replace(")", ",")
        # EL MENSAJE RECIBIDO CORRESPONDE A LAS PARAMETROS DE INICIO DE JUEGO.

        if msg[0:5] == "START":

            game.team_1_structure = int(msg[5:8])
            game.team_2_structure = int(msg[9:12])
            print(game.team_1_structure)
            print(game.team_2_structure)

        else:
            # EL MENSAJE RECIBIDO CORRESPONDE A UNA GENERACION.

            msg = msg.replace("\n", ",")
            sms_len = 0
            print(msg)
            result = []
            buffer = ""
            char = False
            while(sms_len < len(msg)):
                if msg[sms_len] == ',':
                    if msg[sms_len+1] == ',':
                        break
                    sms_len += 1
                    char = True
                    pass
                if msg[sms_len] == '/' and not char:
                    result.append("TEAM 2")
                    sms_len += 1
                    char = True
                if not char:
                    if type(int(msg[sms_len])) == int and msg[sms_len+1] == ',':
                        result.append(int(buffer))
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
    def recv_sms(self, sms):

        print("procesando")



#p = classify_action()
#translated = p.translate_sms("START (4 4 2) (4 3 3)")
#print(translated)
