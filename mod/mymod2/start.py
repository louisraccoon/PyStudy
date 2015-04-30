#!/usr/bin/python
# -*- coding: utf-8 -*-
from common_module_lib import *
print("loaded mymod2 module")


def initModule(systemMessageBox, myMessageBox):
    myModule = Module(systemMessageBox, myMessageBox)
    mainfunction(myModule)
def mainfunction(system):
    print("------mymod2 process start -------")
    while 1:
        message = system.receiveMessage()
        print("[To mymod2]:"+message)
        system.printMessage("mymod2 receive:"+message)