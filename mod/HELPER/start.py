import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

from common_module_lib import *

def initModule(systemMessageBox, myMessageBox):
    myModule = Module(systemMessageBox, myMessageBox)
    mainfunction(myModule)
def mainfunction(system):
    print("------Helper process start -------")
    while 1:
        message = system.receiveMessage()
        print("[To Helper]:"+message)
        system.sendMessage("/Helper how are you?")
        system.printMessage("Helper receive:"+message)
