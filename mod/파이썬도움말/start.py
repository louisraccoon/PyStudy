# -*- coding: utf-8 -*-
import os
from PyQt5.QtCore import QProcess
from common_module_lib import *

def initModule(systemMessageBox, myMessageBox):
    myModule = Module(systemMessageBox, myMessageBox)
    mainfunction(myModule)
def mainfunction(system):
    ####################모듈명 변경시 필수 필요##################
    modulefoldername = "파이썬도움말"# 모듈폴더명과 항상 같아야한다.
    ############################################################

    print("------"+modulefoldername+" process start -------")
    os.chdir('mod/'+modulefoldername) # 모듈 PATH설정
    temppath=os.getcwd()+r'\animation.py'#실행하고자하는 파일
    while 1:
        message = system.receiveMessage()
        if message =="실행":
            system.printMessage(modulefoldername+"모듈이 실행되었습니다.")
            mypreviewer_process=QProcess()
            mypreviewer_process.start('python', [temppath])
        else:
            system.printMessage(" <"+modulefoldername+"> 메시지목록 ")
            system.printMessage("------------------------------------------------")
            system.printMessage("1)실행          ex)'/파이썬도움말 실행'")
            system.printMessage("------------------------------------------------")



