# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:18:51 2015

@author: Ying
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer
#from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from NodeRPCHandler import NodeRPCHandler
from threading import Thread
from NodeInfo import NodeInfo

def add(nodeAddr):
    nodeInfo = NodeInfo()
    print "Node"+ nodeAddr+"has been added"
    return nodeInfo.addActiveNode(nodeAddr)
            
def delete(nodeAddr):
    nodeInfo = NodeInfo()
    print "Node"+ nodeAddr+"has been deleted"
    return nodeInfo.delActiveNode(nodeAddr)
        
def getActiveNodes():
    nodeInfo = NodeInfo()
    return nodeInfo.activeNodes


class Server(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.__port = port
        self.__ip = ip
        self.webServer = SimpleXMLRPCServer((self.__ip, self.__port))
        print "server initialized"

        
    def stopServer(self):
        self.webServer.shutdown(self)
    

        
    def run(self):
        #server = SimpleXMLRPCServer(("localhost", self.__port))
        server = self.webServer
        server.register_introspection_functions()       
        #server.register_instance(NodeRPCHandler())
        server.register_function(add)
        server.register_function(delete)
        server.register_function(getActiveNodes)
        server.serve_forever()


    
    def test(a,b):
        print "test succeeded"
        print a+b    


    