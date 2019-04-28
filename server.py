#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This sample program, based on the one in the standard library documentation, receives incoming messages and echos them back to the sender. It starts by creating a TCP/IP socket.

import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Then bind() is used to associate the socket with the server address. In this case, the address is localhost, referring to the current server, and the port number is 10000.

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.

# Listen for incoming connections
sock.listen(1)


# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

#accept() returns an open connection between the server and client, along with the address of the client. The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall().

#inicio es para ver si ya se puso la informacion de RealMemory, SwapMemory y PageSize
inicio = False
#counter es para saber si es realmem, swapmem o pagesize
counter = 0
try:
    print >>sys.stderr, 'connection from', client_address

    # Receive the data
    while(inicio==False):
        data = connection.recv(256)
        print >>sys.stderr, 'server received "%s"' % data
        if data:
            print >>sys.stderr, 'sending answer back to the client'
            if(counter==0):
                realMem = data
                counter = counter+1
                connection.sendall("Recibio memoria real")
            elif(counter==1):
                swapMem = data
                counter = counter+1
                connection.sendall("Recibio memoria swap")
            elif(counter==2):
                pageSize = data
                counter = counter+1
                connection.sendall("Recibio tamaño de pagina")

            if(counter >2):
                mensaje = 'Recibido, memoria real: %s, memoria swap %s, tamaño de pagina: %s '% (realMem,swapMem,pageSize)
                connection.sendall(mensaje)
                inicio = True

    politica = connection.recv(256)
    mensaje = 'politica: %s' % politica
    connection.sendall(mensaje)

finally:
     # Clean up the connection
    print >>sys.stderr, 'se fue al finally'
    connection.close()

#When communication with a client is finished, the connection needs to be cleaned up using close(). This example uses a try:finally block to ensure that close() is always called, even in the event of an error.


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


