# -*- coding: utf-8 -*-
import os
from PyQt5.QtCore import QProcess
from common_module_lib import *
'''
<모듈 지원 API>
1.system.receiveMessage()
 사용자(또는 시스템, 모듈)로부터 메시지를 받는다.( 받을때까지 기다린다.)
 ex)모듈명 메시지<- 이 메시지를받는다.
2.system.checkMessageEmpty()
자신에게 온 메시지가 없는지 확인한다. 없으면 True 있으면 False 반환
3.system.printMessage("화면에 출력하고자하는 메시지")
사용자 콘솔창에 시스템 메시지를 보낼수 있다.
4.system.sendMessage("/mymod2 howare you?")
원하는 모듈에게 메시지를 보낼수있다.(이를 통해 모듈간에 상호통신이 가능하다.)
'''
def initModule(systemMessageBox, myMessageBox):
    myModule = Module(systemMessageBox, myMessageBox)
    mainfunction(myModule)
def mainfunction(system):
    ############### 모듈 정보 ############################
    modulefoldername = "conversation"# 모듈폴더명과 항상 같아야한다.
    ############################################################
    print("------"+modulefoldername+" process start -------")
    while 1:
        message = system.receiveMessage()# 사용자로부터 입력된 메시지
        resultmsg = analysis_message(message)
        system.printMessage(modulefoldername+": "+resultmsg)
        
def analysis_message(message):
    sendMessage="무슨 의미일까?"
    단어모음 = message.split('.')
    for text in 단어모음:
        if text.find("날씨") != -1:
            sendMessage="오늘 날씨요?"
    return sendMessage
