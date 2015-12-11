# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:24:19 2015

@author: Ying
"""

class Node():
    def __init__(self,port,ip,activeNodes,isOnline = False,isRunning = True):

        self.__activeNodes = []
        self.__ip = ip
        self.__port = port
    
    def getInstance(self):
        return self
        
    def getIP(self):
        return self.__ip
        
    def setIP(self,ipAddr):
        self.__ip = ipAddr
        
    def getPort(self):
        return self.__port
    
    def setPort(self,newPort):
        self.__port = newPort
    
    def setNodeAddr(self,newip, newport):
        self.__ip = newip
        self.__port = newport
    
    def getNodeAddrStr(self):
        return self.__ip + ":" +self.__port
        
    def isRunning(self):
        return self.__isRunning

    def setOnline(self,isOnline):
        self.__isOnline = isOnline
        
    def getActiveNodes(self):
        return self.__activeNodes
    
    def addActiveNode(self, nodeAddr):
        if nodeAddr in self.__activeNodes:
            return False
        else:
            self.__activeNodes.append(nodeAddr)
            return True
    
    def setActiveNodes(self,newActiveNodes):
        self.__activeNodes = newActiveNodes
    
    def delActiveNode(self, nodeAddr):
        if nodeAddr in self.activeNodes:
            self.__activeNodes.remove(nodeAddr)
            return True
        else:
            return False
    
    def clearActiveNodes(self):
        self.__activeNodes = []
        self.__activeNodes.append(self.ip +":" +self.port)
    
    def add(self, nodeAddr):
        print "Node"+ nodeAddr+"has been added"
        return self.__addActiveNode(nodeAddr)
        
    def delete(self, nodeAddr):
        print "Node"+ nodeAddr+"has been deleted"
        return self.__delActiveNode(nodeAddr)
    
    def test(self):
        print self.__ip
        
    
        
    