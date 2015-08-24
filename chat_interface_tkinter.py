#!/usr/bin/python
# -*- coding: utf-8 -*-
# 반드시 파일은 utf-8로 저장할 것 - 중요
import _thread
import time
from chat_interface_func_tkinter import *

class Chat_interface_tkinter():
    #------------------------------------------------------------------------#
     # message communication queue
    #------------------------------------------------------------------------#
    def sendMessage(self,message):
        if message is not None and message != '':
            self.systemqueue.put(message)
    def checkMessageEmpty(self):
        if self.myqueue.empty():
            return True
        else:
            return False
    def receiveMessage(self):
        while self.myqueue.empty():
            time.sleep(0.3)
        message = self.myqueue.get()
        if message is not None and message != '':
            return message
    def parse_Message(self,message):
        COMMAND_CHAR = ' '
        print("명령어1 처리")
        if message is not None and message.find(COMMAND_CHAR) != -1:
            command, value = message.split(COMMAND_CHAR, 1)
            command = command.strip()
            value = value.strip()
            print("명령어2 처리")
            #명령어 분류 및 처리
            if "/print" == command:
                self.displaySystemChat(value)
                print("[To chatInterface] print command execute")

    def displayThread(self):
        print("쓰레드 생성 체크")
        while 1:
            self.parse_Message(self.receiveMessage())
    def __init__(self, systemqueue, myqueue):
        #------------------------------------------------------------------------#
        # graphic user interface
        #------------------------------------------------------------------------#

        self.textHistory = []
        self.textHistoryIndex = 0

        #Create a window
        self.root = Tk()
        self.root.title("PyStudy console")
        self.root.geometry("400x500")
        self.root.resizable(width=FALSE, height=FALSE)

        #Create a Chat window
        self.ChatLog = Text(self.root, bd=0, bg="white", height="8", width="50", font="Arial",)
        self.ChatLog.insert(END, "대화창 활성화..\n")
        self.ChatLog.config(state=DISABLED)

        #Bind a scrollbar to the Chat window
        self.scrollbar = Scrollbar(self.root, command= self.ChatLog.yview, cursor="heart")
        self.ChatLog['yscrollcommand'] = self.scrollbar.set

        #Create the Button to send message
        self.SendButton = Button(self.root, font=30, text="Send", width="12", height=5,
                            bd=0, bg="#FFBF00", activebackground="#FACC2E",
                            command=self.ClickSendAction)

        #Create the box to enter message
        self.EntryBox = Text(self.root, bd=0, bg="white",width="29", height="5", font="Arial")
        self.EntryBox.bind("<Return>", self.DisableEntry)
        self.EntryBox.bind("<KeyRelease-Return>", self.PressSendAction)
        self.EntryBox.bind("<KeyPress>", self.eventKeyPressEntrybox)

        #Place all components on the screen
        self.scrollbar.place(x=376,y=6, height=386)
        self.ChatLog.place(x=6,y=6, height=386, width=370)
        self.EntryBox.place(x=6, y=401, height=30, width=265)
        self.SendButton.place(x=271, y=401, height=30)

        self.systemqueue = systemqueue
        self.myqueue = myqueue
        #시스템으로부터 메시지 듣는 쓰레드 생성
        _thread.start_new_thread(self.displayThread,())

    #------------------------------------------------------------------------#
    # GUI Mouse Event
    #------------------------------------------------------------------------#
    def ClickSendAction(self):
        #Write message to chat window

        EntryText = FilteredMessage(self.EntryBox.get("0.0",END))
        self.textHistoryIndex = 0
        self.textHistory.append(EntryText[:len(EntryText)-1])
        self.InputUserChat(EntryText)
        #Scroll to the bottom of chat windows
        self.ChatLog.yview(END)
        #Erace previous message in Entry Box
        self.EntryBox.delete("0.0",END)
        #Send my mesage to all others
        #s.sendall(EntryText)
    def displayUserChat(self,EntryText):
        #Write message to chat window
        EntryText = FilteredMessage(EntryText)
        self.InputUserChat(EntryText)
        #Scroll to the bottom of chat windows
        self.ChatLog.yview(END)
        #Erace previous message in Entry Box
        self.EntryBox.delete("0.0",END)
    def displaySystemChat(self,EntryText):
        #Write message to chat window
        EntryText+="\n"
        EntryText = FilteredMessage(EntryText)
        self.InputSystemChat(EntryText)
        #Scroll to the bottom of chat windows
        self.ChatLog.yview(END)
        #Erace previous message in Entry Box
        self.EntryBox.delete("0.0",END)
    #------------------------------------------------------------------------#
    # GUI Keyboard Event
    #------------------------------------------------------------------------#
    def PressSendAction(self,event):
        self.EntryBox.config(state=NORMAL)
        self.ClickSendAction()
    def DisableEntry(self,event):
        self.EntryBox.config(state=DISABLED)
    def InputUserChat(self, EntryText):
        if EntryText != '':
            self.ChatLog.config(state=NORMAL)
            if self.ChatLog.index('end') != None:
                LineNumber = float(self.ChatLog.index('end'))-1.0
                self.ChatLog.insert(END, "You: " + EntryText)
                self.ChatLog.tag_add("You", LineNumber, LineNumber+0.4)
                self.ChatLog.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
                self.ChatLog.config(state=DISABLED)
                self.ChatLog.yview(END)

                self.sendMessage("/UserInput "+EntryText)
    def InputSystemChat(self, EntryText):
        if EntryText != '':
            self.ChatLog.config(state=NORMAL)
            if self.ChatLog.index('end') != None:
                LineNumber = float(self.ChatLog.index('end'))-1.0
                self.ChatLog.insert(END, "System: " + EntryText)
                self.ChatLog.tag_add("System", LineNumber, LineNumber+0.7)
                self.ChatLog.tag_config("System", foreground="#2E2EFE", font=("Arial", 12, "bold"))
                self.ChatLog.config(state=DISABLED)
                self.ChatLog.yview(END)
    def eventKeyPressEntrybox(self,event):
        if event.keysym == 'Up':
            if len(self.textHistory) != 0 :

                if self.textHistoryIndex == len(self.textHistory)-1:
                    self.textHistoryIndex = 0
                else:
                    self.textHistoryIndex += 1

                self.EntryBox.delete("0.0",END)
                self.EntryBox.insert(END, self.textHistory[self.textHistoryIndex])
                print(" event kp_up ")
                print("texthistoryindex : %d"  % self.textHistoryIndex)
        elif event.keysym == 'Down':
            if len(self.textHistory) != 0 :
                if self.textHistoryIndex == 0:
                    self.textHistoryIndex = len(self.textHistory)-1
                else:
                    self.textHistoryIndex -= 1
                self.EntryBox.delete("0.0",END)
                self.EntryBox.insert(END, self.textHistory[self.textHistoryIndex])
                print(" event kp_down ")
                print("texthistoryindex : %d"  % self.textHistoryIndex)

    def __del__(self):
        self.sendMessage("/programExit ")

if __name__ == '__main__':
    #모듈을 직접 실행한 경우
    #mychat = Chat_interface_tkinter()
    print("chat_interface_module_self_execute")
    #mychat.displaySystemChat("시스템 작동중입니다.")
    #mychat.root.mainloop()

