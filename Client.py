"""
Created on Wed Dec 16 17:08:53 2015

@author: Ying
"""
import xmlrpclib
from NodeInfo import NodeInfo
from Node import Node
import threading


class Client(threading.Thread):
    def __init__(self,ip,port):
        self.nodeInfo = NodeInfo(port,ip)
        self.nodeInfo.setRunning(True)
        self.nodeInfo.setNodeAddr(ip,port)
        self.nodeInfo.addActiveNode(ip + ":" + str(port))
        
        
    def stopClient(self):      
        self.nodeInfo.setRunning(False)
        
    
    def joinRPC(self,url):
        proxy = xmlrpclib.ServerProxy(url)
        multicall = xmlrpclib.MultiCall(proxy)
        params = self.nodeInfo.getNodeAddrStr()
        multicall.add(params)
        
    def signOffRPC(self,url):
        proxy = xmlrpclib.ServerProxy(url)
        multicall = xmlrpclib.MultiCall(proxy)
        params = self.nodeInfo.getNodeAddrStr()
        multicall.delete(params)
        
    def join(self):
        if (self.nodeInfo.isOnline()):
            ip = raw_input('Input IP to connect to')
            port = raw_input('Input port to connect to')
            self.nodeInfo.setParentNodeAddr(ip+":"+port)
            
            proxy = xmlrpclib.ServerProxy("http://"+self.nodeInfo.getParentNodeAddr()+"/xmlrpc")
            multicall = xmlrpclib.MultiCall(proxy)
            activeNodes = multicall.getActiveNodes()
            
            for node in activeNodes:
                self.nodeInfo.addActiveNode(node)
            
            self.nodeInfo.setOnline = True
            
            for nodeAddr in self.nodeInfo.getActiveNodes():
                if nodeAddr != self.nodeInfo.getNodeAddrStr():
                    self.joinRPC("http://" + nodeAddr + "/xmlrpc")
            return 0
        else:
            print "Something is wrong, node may already exist"
            return -1
    
    def signOff(self):
        currentNodeAddr = self.nodeInfo.getNodeAddrStr()
        
        if self.nodeInfo.isOnline():
            self.nodeInfo.setOnline = False
            
            for nodeAddr in self.nodeInfo.getActiveNodes():
                if nodeAddr != currentNodeAddr:
                    self.signOffRPC("http://"+nodeAddr+"/xmlrpc")
            
            self.nodeInfo.clearActiveNodes()
                