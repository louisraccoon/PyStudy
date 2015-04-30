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

