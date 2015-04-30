import time
from multiprocessing import Queue

class Module:
    def __init__(self, systemqueue, myqueue):
        self.systemqueue = systemqueue
        self.myqueue = myqueue
    def sendMessage(self,message):
        if message is not None and message != '':
            self.systemqueue.put(message)
    def printMessage(self,message):
        if message is not None and message != '':
            self.systemqueue.put("/print "+message)
    def checkMessageEmpty(self):
        if self.myqueue.empty():
            return True
        else:
            return False
    def receiveMessage(self):
        while self.myqueue.empty():
            time.sleep(0.2)
        message = self.myqueue.get()
        if message is not None and message != '':
            return message


