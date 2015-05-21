#!/usr/bin/python
# -*- coding: utf-8 -*-
from common_module_lib import *
print("loaded 학습창 module")
from PyQt5.QtCore import QProcess
import os
def initModule(systemMessageBox, myMessageBox):
    myModule = Module(systemMessageBox, myMessageBox)
    mainfunction(myModule)
def mainfunction(system):
    print("------학습창 process start -------")
    while 1:
        message = system.receiveMessage()
        print("[To 학습창]:"+message)
        system.printMessage("학습창 receive:"+message)
        if message =="실행":
            # Get the current environment end filter out the old
            # PYTHONPATH variable if exists in the environment
            env = [env for env in QProcess.systemEnvironment()
                   if not env.startswith('PYTHONPATH=')]
            # Add your PYTHONPATH
            env.append('PYTHONPATH='+os.getcwd())
            print(env)
            #print(QProcess.systemEnvironment())
            # Create a process, set the environment and run the script
            system.printMessage("학습창 : 실행되었습니다.")
            temppath=os.getcwd()+"\mod\학습창\PyPreviewer.py"
            mypreviewer_process=QProcess()
            #mypreviewer_process.setProcessEnvironment(env)
            print(temppath)
            mypreviewer_process.start('python', [temppath])
            mypreviewer_process.started.connect(lambda: print('학습창ProgramStarted!'))


