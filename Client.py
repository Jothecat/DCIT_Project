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
        
    def stopClient():
        nodeInfo = NodeInfo.getInstance()
        nodeInfo.setRunning(False)
    
    def joinRPC(url):
        nodeInfo = NodeInfo.getInstance()
        
        
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")   
multicall = xmlrpclib.MultiCall(proxy)
multicall.test(22)