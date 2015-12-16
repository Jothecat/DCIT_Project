# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:24:19 2015

@author: Ying
"""

class NodeInfo():

    def __init__(self,port,ip,activeNodes=[],isOnline = False,isRunning = True):
        self.__ip = ip
        self.__port = port
        self.activeNodes = activeNodes
        self.parentNodeAddr = ""
    
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
        return self.isRunning
    
    def setRunning(self, isRunning):
        self.isRunning = isRunning
        
    def isOnline(self):
        return self.isOnline
               
    def setOnline(self,isOnline):
        self.isOnline = isOnline
        
    def getActiveNodes(self):
        return self.activeNodes
    
    def addActiveNode(self, nodeAddr):
        if self.activeNodes != []:
            if nodeAddr in self.activeNodes:
                return False
            else:
                self.activeNodes.append(nodeAddr)
                return True
        else:
            self.activeNodes.append(nodeAddr)
            return True
    
    def setActiveNodes(self,newActiveNodes):
        self.activeNodes = newActiveNodes
    
    def delActiveNode(self, nodeAddr):
        if nodeAddr in self.activeNodes:
            self.activeNodes.remove(nodeAddr)
            return True
        else:
            return False
    
    def clearActiveNodes(self):
        self.activeNodes = []
        self.activeNodes.append(self.ip +":" +self.port)
    
    def add(self, nodeAddr):
        print "Node"+ nodeAddr+"has been added"
        return self.addActiveNode(nodeAddr)
        
    def delete(self, nodeAddr):
        print "Node"+ nodeAddr+"has been deleted"
        return self.delActiveNode(nodeAddr)
    
    def getParentNodeAddr(self):
        return self.parentNodeAddr
    
    def setParentNodeAddr(self, parentNodeAddr):
        self.parentNodeAddr = parentNodeAddr
    
    
    
    
    def test(inp):
        print inp
        
    
 
    