#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser
from common_module_lib import *
print("loaded websearch module")


def initModule(systemMessageBox, myMessageBox):
    myModule = Module(systemMessageBox, myMessageBox)
    mainfunction(myModule)
def mainfunction(system):
    print("------websearch process start -------")
    while 1:
        keyword = system.receiveMessage()
        search(keyword)
def search(keyword):
    print("[To websearch]:"+keyword)
    webbrowser.open("https://www.google.co.kr/webhp?hl=ko#newwindow=1&hl=ko&q="+keyword)
    webbrowser.open("http://search.naver.com/search.naver?where=nexearch&query="+keyword+"&sm=top_hty&fbm=1&ie=utf8")
    webbrowser.open("http://search.naver.com/search.naver?where=nexearch&query="+keyword+"&sm=top_hty&fbm=1&ie=utf8")
    webbrowser.open("http://stackoverflow.com/search?q="+keyword)