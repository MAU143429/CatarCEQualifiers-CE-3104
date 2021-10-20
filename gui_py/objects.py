import board
'''
Esta clase define el comportamiento del jugador en la interfaz
'''
class Player ():

    def __init__(self,image,box,distance,force,position):
        self.image = image
        self.box = box
        self.distance = distance
        self.force = force
        self.position = position
        self.x = 0
        self.y = 0
        self.movement = []

    def getBox(self):
        return self.box

    def setBox(self, new_box):
        table = board.board()
        table.setUse(new_box,True)
        table.setUse(self.box,False)
        self.box = new_box
        self.x = table.getPosx(new_box)
        self.y = table.getPosy(new_box)

    def getDistance(self):
        return self.distance

    def setDistance(self, new_distance):
        self.distance = new_distance

    def getForce(self):
        return self.force

    def setForce(self, new_force):
        self.force = new_force

    def getPos(self):
        return self.position

    def setPos(self, new_pos):
        self.position = new_pos

    def getPosX(self):
        return self.x

    def getPosY(self):
        return self.y

    def getMovements(self):
        return self.movement

    def setMovements(self, new_mov):
        self.movement = new_mov



class Ball ():

    def __init__(self,image,box):
        self.image = image
        self.box = box
        self.x = 0
        self.y = 0

    def getBox(self):
        return self.box

    def setBox(self, new_box):
        table = board.board()
        table.setUse(new_box,True)
        table.setUse(self.box,False)
        self.box = new_box
        self.x = table.getPosx(new_box)
        self.y = table.getPosy(new_box)

    def getPosX(self):
        return self.x

    def getPosY(self):
        return self.y
