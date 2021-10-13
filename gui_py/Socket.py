import socket

import sys

# SE CREA LA ESTRUCTURA DEL SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SE ESCOGEN LA IP Y EL PUERTO EN DONDE SE UBICARÁ EL SOCKET
server_address = ('localhost', 9876)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# SE ABRE LA CONEXION CON EL SOCKET
sock.listen(1)

while True:
    # SE ESPERA LA CONEXION DE UN CLIENTE
    print('waiting for a connection')

    #SE CONECTAN
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # SE CREA UN BUCLE QUE SE QUEDA ESPERANDO POR MENSAJES
        while True:
            data = connection.recv(3600)
            print(data.decode('ascii'))
            msg_rcv = data.decode('ascii')

            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # SE CIERRA LA CONEXION
        connection.close()
