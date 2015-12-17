# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:24:19 2015

@author: Ying
"""
class Singleton(type):  
    def __init__(cls, name, bases, dict):  
        super(Singleton, cls).__init__(name, bases, dict)  
        cls._instance = None  
    def __call__(cls, *args, **kw):  
        if cls._instance is None:  
            cls._instance = super(Singleton, cls).__call__(*args, **kw)  
        return cls._instance  


class NodeInfo(object):
    __metaclass__ = Singleton
    
    def __init__(self,port,ip,isOnline = False,isRunning = True):
        self.__ip = ip
        self.__port = port
        self.activeNodes = []
        self.parentNodeAddr = ""
    
    #def getInstance(self):
        #return self
        
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
        return self.__ip + ":" +str(self.__port)
        
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
        self.activeNodes.append(self.__ip +":" +str(self.__port))
    

    
    def getParentNodeAddr(self):
        return self.parentNodeAddr
    
    def setParentNodeAddr(self, parentNodeAddr):
        self.parentNodeAddr = parentNodeAddr

    def test(inp):
        print inp
        
    
 
    