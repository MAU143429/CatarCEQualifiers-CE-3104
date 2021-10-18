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

    def getBox(self):
        return self.box

    def setBox(self, new_box):
        self.box = new_box
        self.x = board.board().getPosx(new_box)
        self.y = board.board().getPosy(new_box)

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



class Ball ():

    def __init__(self,image,box,goal):
        self.image = image
        self.box = box
        self.goal = goal
        self.x = 0
        self.y = 0

    def getBox(self):
        return self.box

    def setBox(self, new_box):
        self.box = new_box
        self.x = board.board().getPosx(new_box)
        self.y = board.board().getPosy(new_box)

    def getGoal(self):
        return self.goal

    def setGoal(self, new_status):
        self.goal = new_status

    def getPosX(self):
        return self.x

    def getPosY(self):
        return self.y
