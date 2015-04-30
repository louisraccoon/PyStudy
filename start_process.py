#!/usr/bin/python
# -*- coding: utf-8 -*-
from chat_interface_tkinter import *
from multiprocessing import Queue
import importlib
import multiprocessing

from common_func import *

###################################################
#  greencat ver.0.1   modified day 3/26
###################################################

class Main_Process:
    def __init__(self):
        #메인 프로세스의 메세지박스
        self.systemMessageBox = Queue(52)

        #유저모듈명 사전수집
        self.userModuleNameList = getDirectoryList()
        #유저모듈 형식 검사
        #self.userModuleNameList = ['mymod1','mymod2']
        self.userModuleTotalNum = len(self.userModuleNameList)
        self.userModuleQueueList =[]
        self.userModulePIDList=[]
        #GUI 프로세스 생성
        #기본적으로 userModuleNameList[0]에는  채팅창 프로세스가 들어있다.
        chatModuleMessageBox = Queue(10)
        pid = multiprocessing.Process(target=call_chat_interface, args=(self.systemMessageBox, chatModuleMessageBox ))
        pid.start()
        self.userModuleQueueList.append(chatModuleMessageBox)
        self.userModulePIDList.append(pid)
        #각 유저모듈 생성 작업
        for i,v in enumerate(self.userModuleNameList):
            print("------- {0} 번재 모듈 -------------".format(i+1))
            print("Index: {0}, Value: {1}".format(i+1, v))
            #유저모듈메시지박스 생성
            userModuleMessageBox = Queue(10)
            self.userModuleQueueList.append(userModuleMessageBox)
            # 동적 모듈로딩
            tempModulePath = 'mod.'+self.userModuleNameList[i]+'.start'
            module = importlib.import_module(tempModulePath)
            #print(getattr(module, "Module"))
            #print(getattr(module, "myfunction"))

            #모듈속 initModule함수  myfunc로 이름 재정의
            myfunc = getattr(module, "initModule")
            # 모듈용 프로세스 생성
            pid = multiprocessing.Process(target=myfunc, args=(self.systemMessageBox, userModuleMessageBox))
            pid.start()
            # 모듈PID관리 리스트에 추가
            self.userModulePIDList.append(pid)
        self.userModuleNameList.insert(0,"chat")
        self.running()
    def sendMessage(self,MessageBoxId,message):
        self.userModuleQueueList[MessageBoxId].put(message)
    def receiveSystemMessage(self):
        while self.systemMessageBox.empty():
            time.sleep(0.05)
        message = self.systemMessageBox.get()
        if message is not None and message != '':
            return message
    def parse_Message(self,message):
        COMMAND_CHAR = ' '
        if message is not None and message.find(COMMAND_CHAR) != -1:
            command, value = message.split(COMMAND_CHAR, 1)
            command = command.strip()
            value = value.strip()
            #명령어 분류 및 처리
            if "/print" == command:
                print("[system]:"+value)
                self.sendMessage(0,"/print "+value)
            elif "/UserInput" == command:
                if value[0] != '/':
                    #user말 따라하기
                    print("[system]: user say "+value)
                    self.sendMessage(0,"/print user say "+value)
                elif value.find(' ') != -1 :
                    command, value = value.split(' ', 1)
                    command = command[1:]
                    #모듈에게 온 메세지 전달
                    if command in self.userModuleNameList:
                        moduleIndex = self.userModuleNameList.index(command)
                        self.sendMessage(moduleIndex, value)
                    else:
                        self.sendMessage(0,"/print 존재하지않는 모듈명입니다.\n( ex: '/모듈명 메시지' )")
                else:
                        self.sendMessage(0,"/print 존재하지않는 모듈명입니다.\n( ex: '/모듈명 메시지' )")
            elif "/programExit" == command:
                quit()
            elif command[0] == '/':
                command = command[1:]
                #모듈에게 온 메세지 전달
                if command in self.userModuleNameList:
                    moduleIndex = self.userModuleNameList.index(command)
                    self.sendMessage(moduleIndex, value)
                else:
                    self.sendMessage(0,"/print 존재하지않는 모듈명입니다.\n( ex: '/모듈명 메시지' )")


    def running(self):
        while 1:
            #시스템 메시지 박스 불러오기
            self.parse_Message(self.receiveSystemMessage())
    def __del__(self):
        for i,v in enumerate(self.userModulePIDList):
            self.userModulePIDList[i].terminate()
            #print('TERMINATED:', self.userModulePIDList[i], "is_alive?:",self.userModulePIDList[i].is_alive())
            self.userModulePIDList[i].join()
            print ( self.userModulePIDList[i], "is alive?:", self.userModulePIDList[i].is_alive())


def call_chat_interface(systemMessageBox, myMessageBox):
    mychat = Chat_interface_tkinter(systemMessageBox, myMessageBox)
    mychat.root.mainloop()
    #채팅창 종료시 채팅프로세스는 여기서부터 실행
    mychat.__del__()
    mychat.root.quit()


if __name__ == '__main__':
    #모듈을 직접 실행한 경우
    main=Main_Process()
    quit(0)




