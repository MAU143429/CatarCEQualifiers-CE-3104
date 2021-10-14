import gui
import Socket
from threading import *

'''
Este metodo inicializara el socket
'''
def start_socket():
    sock = Socket.Socket()
    sock.init_Socket()

'''
Este metodo inicializara el gui
'''
def start_gui():
    interface = gui.gui()
    interface.init_gui()

'''
Se definen hilos y se inicializan posteriormente
'''
t1 = Thread(target=start_socket)
t2 = Thread(target=start_gui)

t1.start()
t2.start()



