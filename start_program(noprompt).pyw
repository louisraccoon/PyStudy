#!/usr/bin/python
# -*- coding: utf-8 -*-
from chat_interface_tkinter import *
from multiprocessing import Queue
import importlib
import multiprocessing

from common_func import *

###################################################
#  greencat ver.0.2   modified day 5/31
###################################################

class Main_Process:
    def __init__(self):
        #메인 프로세스의 메세지박스
        self.systemMessageBox = Queue(53)

        #유저모듈명 사전수집
        self.userModuleNameList = getDirectoryList()
        #유저모듈 형식 검사
        #self.userModuleNameList = ['mymod1','mymod2']
        self.userModuleTotalNum = len(self.userModuleNameList)
        self.userModuleQueueList =[]
        self.userModulePIDList=[]
        #GUI 프로세스 생성
        #기본적으로 userModuleNameList[0]에는  채팅창 프로세스가 들어있다.
        self.chatModuleMessageBox = Queue(10)
        self.chatpid = multiprocessing.Process(target=call_chat_interface, args=(self.systemMessageBox, self.chatModuleMessageBox ))
        self.chatpid.start()
        self.userModuleQueueList.append(self.chatModuleMessageBox)
        self.userModulePIDList.append(self.chatpid)
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
        self.userModuleNameList.insert(0,"chating_module")
        self.parse_Message("/UserInput /학습창 실행")
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
                    #print("[system]: user say "+value)
                    #self.sendMessage(0,"/print user say "+value)
                    self.parse_Message("/UserInput /conversation "+value)
                elif value.find('/reload') != -1:
                    self.reload_modulelist()
                    self.sendMessage(0,"/print 모든 모듈을 다시 불러옵니다.")
                elif value.find(' ') != -1 :
                    command, value = value.split(' ', 1)
                    command = command[1:]# 모듈명 앞에 붙은 슬래시 제거( ex:/mymod1 -> mymod1
                    #모듈에게 온 메세지 전달
                    if command in self.userModuleNameList:
                        moduleIndex = self.userModuleNameList.index(command)
                        self.sendMessage(moduleIndex, value)
                    else:
                        self.sendMessage(0,"/print 존재하지않는 모듈명입니다.\n( ex: '/모듈명 메시지' )")
                        self.print_userModuleNameList()
                else:
                    modulename = value[1:]
                    print(modulename)
                    #모듈에게 온 메세지 전달
                    if modulename in self.userModuleNameList:
                        self.sendMessage(0,"/print 모듈에 전송할메시지도 입력해주세요\n( ex: '/모듈명 메시지' )")
                    else:
                        self.sendMessage(0,"/print 존재하지않는 모듈명입니다.\n( ex: '/모듈명 메시지' )")
                        self.print_userModuleNameList()
                        self.sendMessage(0,"/print 모듈목록 새로고침( ex: '/reload' )")
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
                    self.print_userModuleNameList()

    def running(self):
        while 1:
            #시스템 메시지 박스 불러오기
            self.parse_Message(self.receiveSystemMessage())
    def print_userModuleNameList(self):
        self.sendMessage(0,"/print <사용가능한 모듈 목록>")
        for moduleName in self.userModuleNameList:
            self.sendMessage(0,"/print ◎"+moduleName)
    def reload_modulelist(self):
        for i,v in enumerate(self.userModulePIDList):
            if i !=0 :
                self.userModulePIDList[i].terminate()
                self.userModulePIDList[i].join()
        #유저모듈명 사전수집
        self.userModuleNameList = getDirectoryList()
        #유저모듈 형식 검사
        #self.userModuleNameList = ['mymod1','mymod2']
        self.userModuleTotalNum = len(self.userModuleNameList)
        self.userModuleQueueList =[]
        self.userModulePIDList=[]
        #GUI 프로세스 생성
        #기본적으로 userModuleNameList[0]에는  채팅창 프로세스가 들어있다.
        self.userModuleQueueList.append(self.chatModuleMessageBox)
        self.userModulePIDList.append(self.chatpid)
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
        self.userModuleNameList.insert(0,"chating_module")
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




