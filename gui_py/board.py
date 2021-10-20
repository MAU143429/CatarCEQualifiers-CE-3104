import box

table = []
'''
Esta clase se encarga de crear la matriz que permitira tener el control de los jugadores y sus movimientos
'''
class board():
    global table
    '''
    Constructor de la clase, define algunos valores como las filas y columnas de la matriz
    '''
    def __init__(self):
        self.boxes = 1
        self.ROWS = 12   # Cantidad de filas
        self.COLUMN = 24 # Cantidad de columnas
        self.DIMENSION = 50 # Dimension de cada casilla

    '''
    Este metodo crea el tablero, anidando listas de objetos box
    '''
    def create_board(self):
        COORDX = 0
        COORDY = 0
        current_row = []

        while (self.ROWS > 0):
            while(self.COLUMN > 0):
                new_box = box.box(self.boxes,COORDX, COORDY)
                current_row.append(new_box)
                COORDX += self.DIMENSION
                self.boxes += 1
                self.COLUMN -= 1
            COORDX = 0
            table.append(current_row)
            current_row = []
            COORDY += self.DIMENSION
            self.COLUMN = 24
            self.ROWS -= 1
        self.ROWS = 12

    def getPosx(self,box):
        row = box // 24
        column = (box % 24)-1
        return table[row][column].get_posX()

    def getPosy(self,box):
        row = box // 24
        column = (box % 24)-1
        return table[row][column].get_posY()

    def setUse(self,box,status):
        row = box // 24
        column = (box % 24)-1
        table[row][column].use_Status(status)

    def getUse(self,box):
        row = box // 24
        column = (box % 24)-1
        return table[row][column].getUse()




    '''
    ELIMINAR ESTOS METODOSSSSS AL FINAL DEL PROYECTO.
    '''
    def print_boxes(self):
        rows = 0
        cols = 0
        print(" --> [ ")
        while (rows < 12):
            print(" [ ")
            while(cols < 24):
                print(str(board[rows][cols].get_num_box()) + ",")
                cols += 1
            print( " ] , " )
            cols = 0
            rows += 1
        print(" ] <--- ")

    def print_posx(self):
        rows = 0
        cols = 0
        print(" --> [ ")
        while (rows < 12):
            print(" [ ")
            while(cols < 24):
                print(str(board[rows][cols].get_posX()) + ",")
                cols += 1
            print( " ] , " )
            cols = 0
            rows += 1
        print(" ] <--- ")

    def print_posy(self):
        rows = 0
        cols = 0
        print(" --> [ ")
        while (rows < 12):
            print(" [ ")
            while(cols < 24):
                print(str(board[rows][cols].get_posY()) + ",")
                cols += 1
            print( " ] , " )
            cols = 0
            rows += 1
        print(" ] <--- ")






