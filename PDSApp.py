# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:34:45 2015

@author: Daria
"""

import socket

def main():
    print 'main main main'
    port = getPort()
    print 'Port is: ', port
    getIP()


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