# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:55:04 2015

@author: Ying
"""
import threading
from NodeInfo import NodeInfo

class Node(threading.Thread):
   def __init__(self,client, server):
       self.client = client
       self.server = server
       
       serverThread = server
       serverThread.start()
       
       self.client.run()
       
   def run(self):
       isRunning = True
       
       while(isRunning):
           command = raw_input('Input Command:')
           if command == "join":
               self.client.join()
           elif (command == "signoff"):
               self.client.signOff()
           elif command == "stop":
               nodeInfo = NodeInfo.getInstance()
               self.client.signOff()
               nodeInfo.setRunning(False)
               isRunning = False
               break
           else:
               print "Bad Input, Try join, signoff or stop"