# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:34:45 2015

@author: Daria
"""

import socket
from Client import Client
from Server import Server
from Node import Node
from threading import Thread

def main():
    port = getPort()
    client = Client(getIP(), port)
    server = Server(port)
    readerThread = Thread(target = Node(client, server), args = [])
    readerThread.start()
    #getIP()


def getPort():
    port = 3344
    print 'Default port: ', str(port)

    change = raw_input('Change? (y\\n)\n')
    if change == 'y':
        newPort = raw_input('Input correct port: ')
        if newPort != -1:
            return  newPort
    return port

def getIP():
    ipAddress = None
    hostname = socket.gethostname()
    ipAddress = socket.gethostbyname(hostname)
    print 'Default IP Adress: ', ipAddress
    change = raw_input('Change? (y\\n)\n')
    if change == 'y':
        newIpAddress = raw_input('Input correct IP: ')
        if newIpAddress != None:
            return newIpAddress
    return ipAddress



if __name__ == "__main__":
    main()