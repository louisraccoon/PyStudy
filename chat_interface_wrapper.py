#!/usr/bin/python
# -*- coding: utf-8 -*-
# 반드시 파일은 utf-8로 저장할 것 - 중요


class Chat_interface_wrapper:
    def sendUserChatToCommunicationQueue(self, queue, entrytext):
        print("sendUserToQueue: "+entrytext+"\n")
    def displaySystemChat(self, entrytext):
        print("displaySystem: "+entrytext+"\n")


if __name__ == '__main__':
    #모듈을 직접 실행한 경우
    #mychat = Chat_interface_tkinter()
    print("Chat_interface_wrapper_module_self_execute")
    #mychat.InputSystemChatAction("시스템 작동중입니다.")
    #mychat.root.mainloop()

else:
    print("import Chat_interface_wrapper")