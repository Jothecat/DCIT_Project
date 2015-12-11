# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:24:19 2015

@author: Ying
"""

class Node():
    def __init__(self,port,ip,isOnline,isRunning,activeNodes):
        self.isOnline = False
        self.isRunning = True
        self.activeNodes = []
        self.ip = ip
        self.port = port
    
    def getInstance(self):
        return self
        
    def getIP(self):
        return self.ip
        
    def setIP(self,ipAddr):
        self.ip = ipAddr
        
    def getPort(self):
        return self.port
    
    def setPort(self,newPort):
        self.port = newPort
    
    def setNodeAddr(self,newip, newport):
        self.ip = newip
        self.port = newport
    
    def getNodeAddrStr(self):
        return self.ip + ":" +self.port
        
    def isRunning(self):
        return self.isRunning

    def setOnline(self,isOnline):
        self.isOnline = isOnline
        
    def getActiveNodes(self):
        return self.activeNodes
    
    def addActiveNode(self, nodeAddr):
        if nodeAddr in self.activeNodes:
            return False
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
        
    
        
    