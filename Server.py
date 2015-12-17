# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:18:51 2015

@author: Ying
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer
#from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from NodeRPCHandler import NodeRPCHandler
from threading import Thread

class Server(Thread):
    def __init__(self,port):
        Thread.__init__(self)
        self.__port = port
        self.webServer = SimpleXMLRPCServer(("localhost", self.__port))
        print "server initialized"

        
    def stopServer(self):
        self.webServer.shutdown(self)
           
    def run(self):
        #server = SimpleXMLRPCServer(("localhost", self.__port))
        server = self.webServer
        server.register_introspection_functions()       
        server.register_instance(NodeRPCHandler())
        server.serve_forever()
        print "server is running"
        


    