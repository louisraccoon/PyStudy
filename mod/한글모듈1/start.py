#!/usr/bin/python
# -*- coding: utf-8 -*-
from common_module_lib import *
print("loaded mymod1 module")

def initModule(systemMessageBox, myMessageBox):
    myModule = Module(systemMessageBox, myMessageBox)
    mainfunction(myModule)
def mainfunction(system):
    print("------mymod1 process start -------")
    while 1:
        message = system.receiveMessage()
        print("[To mymod1]:"+message)
        system.sendMessage("/mymod2 how are you?")
        system.printMessage("mymod1 receive:"+message)
        한글함수()

def 한글함수():
    잘되나 = "한글테스트"
    화면출력(잘되나)
def 화면출력(출력할문장):
    print(출력할문장)

