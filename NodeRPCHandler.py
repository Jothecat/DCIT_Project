# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 01:15:48 2015

@author: Ying
"""
from NodeInfo import NodeInfo
from NodeInfo import Singleton

class NodeRPCHandler:
    def add(nodeAddr):
        nodeInfo = NodeInfo()
        print "Node"+ nodeAddr+"has been added"
        return nodeInfo.addActiveNode(nodeAddr)
        
    def delete(self, nodeAddr):
        nodeInfo = NodeInfo()
        print "Node"+ nodeAddr+"has been deleted"
        return nodeInfo.delActiveNode(nodeAddr)
    
    def getActiveNodes():
        nodeInfo = NodeInfo()
        return nodeInfo.activeNodes
    
    def test():
        print "test succeeded"