"""
Created on Wed Dec 16 17:08:53 2015

@author: Ying
"""
import xmlrpclib
from NodeInfo import NodeInfo
from threading import Thread


class Client(Thread):

    def __init__(self,ip,port):
        nodeInfo = NodeInfo(port,ip)
        nodeInfo.setRunning(True)
        nodeInfo.setNodeAddr(ip,port)
        nodeInfo.addActiveNode(ip + ":" + str(port))

        
    def stopClient(self): 
        nodeInfo = NodeInfo()
        nodeInfo.setRunning(False)
        
    
    def joinRPC(self,url):
        nodeInfo = NodeInfo()
        proxy = xmlrpclib.ServerProxy(url)
        #multicall = xmlrpclib.MultiCall(proxy)
        params = nodeInfo.getNodeAddrStr()
        proxy.add(params)
        
    def signOffRPC(self,url):
        nodeInfo = NodeInfo()
        proxy = xmlrpclib.ServerProxy(url)
        #multicall = xmlrpclib.MultiCall(proxy)
        params = nodeInfo.getNodeAddrStr()
        proxy.delete(params)
        
    def join(self):
        nodeInfo = NodeInfo()
        if (nodeInfo.isOnline()==False):
            ip = raw_input('Input IP to connect to:')
            port = raw_input('Input port to connect to:')
            nodeInfo.setParentNodeAddr(ip+":"+str(port))
            
            proxy = xmlrpclib.ServerProxy("http://"+self.nodeInfo.getParentNodeAddr()+"/xmlrpc")
            #multicall = xmlrpclib.MultiCall(proxy)
            activeNodes = proxy.getActiveNodes()
            
            if(activeNodes != []):
                for node in activeNodes:
                    nodeInfo.addActiveNode(node)
            
            nodeInfo.setOnline = True
            
            for nodeAddr in nodeInfo.getActiveNodes():
                if nodeAddr != nodeInfo.getNodeAddrStr():
                    self.joinRPC("http://" + nodeAddr + "/xmlrpc")
                    print "successfully joined"
            return 0
        else:
            print "Something is wrong, node may already exist"
            return -1
    
    def signOff(self):
        nodeInfo = NodeInfo()
        currentNodeAddr = nodeInfo.getNodeAddrStr()
        
        if nodeInfo.isOnline():
            nodeInfo.setOnline = False
            
            for nodeAddr in nodeInfo.getActiveNodes():
                if nodeAddr != currentNodeAddr:
                    self.signOffRPC("http://"+nodeAddr+"/xmlrpc")
            
            nodeInfo.clearActiveNodes()

    def run(self):
        class Runnable(Thread):
            def run(self):
                nodeInfo = NodeInfo()
                #while nodeInfo.isRunning():
                    #if nodeInfo.isOnline():
                        #pass
        Runnable().start()
