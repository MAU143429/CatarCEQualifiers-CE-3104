import box

class board():

    def __init__(self):
        self.board = []
        self.boxes = 1
        self.ROWS = 12   # Cantidad de filas
        self.COLUMN = 24 # Cantidad de columnas
        self.DIMENSION = 50 # Dimension de cada casilla



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
            self.board.append(current_row)
            current_row = []
            COORDY += self.DIMENSION
            self.COLUMN = 24
            self.ROWS -= 1
        self.ROWS = 12


    def print_boxes(self):
        rows = 0
        cols = 0
        print(" --> [ ")
        while (rows < 12):
            print(" [ ")
            while(cols < 24):
                print(str(self.board[rows][cols].get_num_box()) + ",")
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
                print(str(self.board[rows][cols].get_posX()) + ",")
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
                print(str(self.board[rows][cols].get_posY()) + ",")
                cols += 1
            print( " ] , " )
            cols = 0
            rows += 1
        print(" ] <--- ")






