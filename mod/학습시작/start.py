# -*- coding: utf-8 -*-
import os
from PyQt5.QtCore import QProcess
from common_module_lib import *

def initModule(systemMessageBox, myMessageBox):
    myModule = Module(systemMessageBox, myMessageBox)
    mainfunction(myModule)
'''
    <모듈 설명서>
    모듈명 변경시 수정이 필요한 부분
    1.modulefoldername ( 모듈폴더명)
    2.runFileName( 파일명 )
'''
def mainfunction(system):
    ############### 모듈 정보 ############################
    modulefoldername = "학습시작"# 모듈폴더명과 항상 같아야한다.
    runFileName = r"\chart.py"# 모듈에서 실행할 파이썬 파일 꼭 파일명앞에 \(역슬래시 붙여주어야한다.)
    ############################################################

    print("------"+modulefoldername+" process start -------")
    os.chdir('mod/'+modulefoldername) # 모듈 실행 PATH변경
    temppath=os.getcwd()+runFileName
    while 1:
        message = system.receiveMessage()
        if message =="실행":
            system.printMessage(modulefoldername+"모듈이 실행되었습니다.")
            mypreviewer_process=QProcess()
            mypreviewer_process.start('python', [temppath])
        else:
            system.printMessage(" <"+modulefoldername+"> 메시지목록 ")
            system.printMessage("------------------------------------------------")
            system.printMessage("1)실행          ex)'/학습창 실행'")
            system.printMessage("------------------------------------------------")
