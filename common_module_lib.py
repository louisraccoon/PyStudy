import time
from multiprocessing import Queue

class Module:
    def __init__(self, systemqueue, myqueue):
        self.systemqueue = systemqueue
        self.myqueue = myqueue
    def sendMessage(self,message):# 메시지 보내기
        if message is not None and message != '':
            self.systemqueue.put(message)
    def printMessage(self,message):#콘솔창 메시지 보내기
        if message is not None and message != '':
            self.systemqueue.put("/print "+message)
    def checkMessageEmpty(self):#시스템으로부터 메시지 있는지 체크
        if self.myqueue.empty():
            return True
        else:
            return False
    def receiveMessage(self):#메시지 받기(받을때까지 기다린다.)
        while self.myqueue.empty():
            time.sleep(0.2)
        message = self.myqueue.get()
        if message is not None and message != '':
            return message


