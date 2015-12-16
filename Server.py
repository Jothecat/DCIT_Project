# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:18:51 2015

@author: Ying
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer
#from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from NodeInfo import NodeInfo
from threading import Thread

class Server(Thread):

    def __init__(self, port):
        self.__port = port
        self.webServer = SimpleXMLRPCServer(("localhost", self.__port))

    def __call__(self):
        print 'server is called'
        pass
        
    def stopServer(self):
        self.webServer.shutdown(self)
           
    def run(self):
        print 'server run forever'
        server = self.webServer
        server.register_introspection_functions()
        
        server.register_instance(NodeInfo())
        server.serve_forever()
