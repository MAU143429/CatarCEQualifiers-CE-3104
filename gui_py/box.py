'''
Esta clase crea los objetos casilla que se usan para mover jugadores
'''

class box():
    '''
    Constructor principal de la clase
    '''
    def __init__(self , number , posx, posy):
        self.number = number
        self.x = posx
        self.y = posy
        self.inUse = False
    '''
    Metodo que retorna el numero de casilla
    '''
    def get_num_box(self):
        return self.number
    '''
    Metodo que retorna la posicion en X de una casilla
    '''
    def get_posX(self):
        return self.x
    '''
    Metodo que retorna la posicion en Y de una casilla
    '''
    def get_posY(self):
        return self.y

    def getUse(self):
        return self.inUse

    def use_Status(self, status):
        self.inUse = status

