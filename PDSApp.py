# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:34:45 2015

@author: Daria
"""

def main():
    print 'main main main'
    port = getPort()
    print 'Port is: ', port


def getPort():
    port = 3344
    print 'Default port: ', str(port)

    answer = raw_input('Change? (y\\n)\n')
    if answer == 'y':
        newPort = raw_input('Input correct port: ')
    if newPort != -1:
        return  newPort

    return port

if __name__ == "__main__": main()