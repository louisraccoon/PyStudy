# -*- coding: utf-8 -*-
import sys
import os
import codecs
import binascii
import time

from PyQt5.QtCore import QFile, QIODevice, QTextStream, QProcess, QUrl, QRegExp, Qt,QByteArray
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog,QSizePolicy, QLineEdit,QInputDialog,QToolBar,QMainWindow, QMessageBox, QWidget, QPlainTextEdit, QSplashScreen)
from PyQt5.QtWebKitWidgets import QWebPage, QWebView
from ui_PyPreviewer import Ui_MainWindow



class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.start_logo()

        self.setupUi(self)

        #self.centralWidget = PyPreviewer(self)
        #self.setCentralWidget(self.centralWidget)
        self.setupEditor()

        self.setWindowIcon(QIcon('PyPreviewer.ico'))


        #메뉴 이벤트 생성
        self.createEvent()

        self.dirty = False
        self.plainTextEdit_2.textChanged.connect(self.setDirty)
        self.fileName = None


        #web view
        #self.exampleView.load(QUrl("http://www.google.com"))
        self.startfilepath=os.getcwd() +"/PyStudy_web/Main.html"
        self.exampleView.load(QUrl.fromLocalFile(self.startfilepath))
        self.locationEdit = QLineEdit(self)
        self.locationEdit.setSizePolicy(QSizePolicy.Expanding,
                self.locationEdit.sizePolicy().verticalPolicy())
        self.locationEdit.returnPressed.connect(self.changeLocation)

        toolBar = QToolBar()
        self.addToolBar(toolBar)
        self.insertToolBarBreak(toolBar)
        toolBar.addAction(self.exampleView.pageAction(QWebPage.Back))
        toolBar.addAction(self.exampleView.pageAction(QWebPage.Forward))
        toolBar.addAction(self.action_myHome)
        toolBar.addAction(self.exampleView.pageAction(QWebPage.Reload))
        #toolBar.addAction(self.exampleView.pageAction(QWebPage.Stop))
        toolBar.addWidget(self.locationEdit)



        #사용자 입력 파이썬 파일 실행
        print ('Connecting process')
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.SeparateChannels)
        self.process.setInputChannelMode(QProcess.ManagedInputChannel)

        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)
        self.process.started.connect(lambda: print('ExampleProgramStarted!'))
        self.process.finished.connect(lambda:print('ExampleProgramFinished!'))
        print('Starting process')
        #self.process.start('python', ['ExampleTest.py'])

    def start_logo(self):
        img_logo = QPixmap('pystudylogo.png')
        self.splash = QSplashScreen(img_logo, Qt.WindowStaysOnTopHint)
        self.splash.setMask(img_logo.mask())
        self.splash.show()
        time.sleep(1.8)
        self.splash.close()
    def show_logo(self):
        img_logo = QPixmap('pystudylogo.png')
        self.splash = QSplashScreen(img_logo, Qt.WindowStaysOnTopHint)
        self.splash.setMask(img_logo.mask())
        self.splash.show()
        self.splash.repaint()
    def createEvent(self):
        self.ProgramRunButton.clicked.connect(self.clickAction_ProgramRunButton)
        self.ProgramStopButton.clicked.connect(self.clickAction_ProgramStopButton)
        self.actionRun.triggered.connect(self.clickAction_ProgramRunButton)
        self.actionStop.triggered.connect(self.clickAction_ProgramStopButton)
        self.ClearButton.clicked.connect(self.clickAction_ProgramEraseButton)
        self.actionClear.triggered.connect(self.clickAction_ProgramEraseButton)
        self.actionNew_File.triggered.connect(self.clickAction_fileNew)
        self.actionFile_Open.triggered.connect(self.clickAction_fileOpen)
        self.actionFile_Save.triggered.connect(self.clickAction_fileSave)
        self.actionFile_Save_as.triggered.connect(self.clickAction_fileSaveAs)
        self.action_example.triggered.connect(self.clickAction_exampleOpen)
        self.actionPythonHelp.triggered.connect(self.clickAction_PythonHelp)
        self.MessagepushButton.clicked.connect(self.clickAction_MessagePushButton)
        self.actionStyleSheet_default.triggered.connect(self.clickAction_styleDefault)
        self.actionStyleSheet_Black.triggered.connect(self.clickAction_styleBlack)
        self.actionStyleSheet_Load.triggered.connect(self.clickAction_styleLoad)
        self.actionAbout_PyStudy.triggered.connect(self.show_logo)
        self.action_myHome.triggered.connect(self.go_myHome)
        self.action_exit.triggered.connect(self.close)
    def setDirty(self):
        #'On change of text in textEdit window, set the flag "dirty" to True''
        if self.dirty:
            return True
        self.dirty = True
        self.updateStatus('소스 수정중...')

    def clearDirty(self):
        #'''Clear the dirty flag and update status'''
        self.dirty = False

    def updateStatus(self, message):
        if self.fileName is not None:
            flbase = os.path.basename(self.fileName)
            self.setWindowTitle("PyStudy Simple Editor - " + flbase + "[*]" )
            self.statusBar().showMessage(message, 3000)
        self.setWindowModified(self.dirty)
    def clickAction_exampleOpen(self):
        fname, filter = QFileDialog.getOpenFileName(self, "예제파일 열기창", '.', "HTML File(*.html *.htm)")
        if not (fname == ""):
            #self.exampleView.load(QUrl(fname))
            self.exampleView.setUrl(QUrl.fromLocalFile(fname))
            #self.plainTextEdit_2.setPlainText(codecs.open(fname, "r", "utf-8" ).read())
            #self.fileName = fname
        else:
            return
        self.updateStatus('example File opened.')
    def clickAction_exampleDirectOpen(self,fname):
        if not (fname == ""):
            fname = os.getcwd()+r"\\"+fname
            print(fname)
            self.exampleView.setUrl(QUrl.fromLocalFile(fname))
        else:
            return
        self.updateStatus('example File opened.')

    def clickAction_fileNew(self):
        #'''Clear the editor window for a new file with name specified in fileSaveAs method.'''
        self.plainTextEdit_2.clear()
        self.statusBar().showMessage('새 소스파일 생성', 8000)
        self.dirty = False
        self.fileName = None

    def clickAction_fileOpen(self):
        fname, filter = QFileDialog.getOpenFileName(self, "소스파일 열기창", '.', "Python File(*.py)")
        if not (fname == ""):
            self.plainTextEdit_2.setPlainText(codecs.open(fname, "r", "utf-8" ).read())
            self.fileName = fname
        else:
            return
        self.clearDirty()
        self.updateStatus('File opened.')


    def clickAction_fileSave(self):
        if self.fileName is None:
            return self.clickAction_fileSaveAs()
        else:
            fname = self.fileName
            fl = codecs.open(fname, "w", "utf-8" )
            tempText = self.plainTextEdit_2.toPlainText()
            if tempText:
                fl.write(tempText)
                fl.close()
                self.clearDirty()
                self.updateStatus('Saved file')
                return True
            else:
                self.statusBar().showMessage('파일 저장 실패 ...', 5000)
                return False

    def clickAction_fileSaveAs(self):
        path = self.fileName if self.fileName is not None else "."
        fname,filter = QFileDialog.getSaveFileName(self,
                        "다른이름으로 저장", path, "Python File(*.py)")
        if fname:
            if "." not in fname:
                fname += ".py"
            self.fileName = fname
            self.clickAction_fileSave()
            self.statusBar().showMessage('SaveAs file' + fname, 8000)
            self.clearDirty()
    def clickAction_ProgramRunButton(self):
        self.clickAction_fileSave()
        self.process.start('python', [self.fileName],QIODevice.ReadWrite)
    def clickAction_ProgramStopButton(self):
        self.process.kill()
        self.append_plainTextEdit_3("\n\n프로세스 정지 with exit code "+str(self.process.exitCode())+"\n\n")
    def clickAction_ProgramEraseButton(self):
        self.plainTextEdit_3.clear()
    def append_plainTextEdit_3(self, text):
        cursor = self.plainTextEdit_3.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        #self.output.ensureCursorVisible()

    def stdoutReady(self):
        text = str(self.process.readAllStandardOutput(), "utf-8")
        self.append_plainTextEdit_3(text)

    def stderrReady(self):
        text = str(self.process.readAllStandardError(), "utf-8")
        self.append_plainTextEdit_3(text)

    def clickAction_PythonHelp(self):
        temppath=os.path.abspath('..')+r"\파이썬도움말\animation.py"
        tempoption = os.path.abspath('..')+r"\파이썬도움말"
        pythonhelp_process=QProcess()
        pythonhelp_process.start('python', [temppath,tempoption])
        pythonhelp_process.started()
        #  TypeError: native Qt signal is not callable
    def clickAction_MessagePushButton(self):
        temp = self.messagelineEdit.text()
        self.append_plainTextEdit_3(temp)
        self.append_plainTextEdit_3("\n")
        bArray = QByteArray()
        bArray.append(temp)
        bArray.append("\n")
        if( self.process.write(bArray) == -1):
            print("chlidprocess write error")
        self.messagelineEdit.clear()
    def clickAction_styleLoad(self):
        fname, filter = QFileDialog.getOpenFileName(self, "QT스타일시트파일 불러오기", '.', "Qt-StyleSheet(*.qss)")
        if fname:
            file = QFile(fname)
            file.open(QFile.ReadOnly)
            styleSheet = file.readAll()
            styleSheet = str(styleSheet, encoding='utf8') # Python v3.
            self.setStyleSheet(styleSheet)
            print ("test")
    def clickAction_styleDefault(self):
        self.set_StyleSheet("default")
    def clickAction_styleBlack(self):
        self.set_StyleSheet("black")
    def set_StyleSheet(self, sheetName):
        if sheetName:
            file = QFile('stylesheet/%s.qss' % sheetName.lower())
            file.open(QFile.ReadOnly)
            styleSheet = file.readAll()
            styleSheet = str(styleSheet, encoding='utf8') # Python v3.
            self.setStyleSheet(styleSheet)

    def setupEditor(self):
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)

        self.editor = self.plainTextEdit_2
        self.editor.setFont(font)
        self.highlighter = Highlighter(self.editor.document())

    def changeLocation(self):
        url = QUrl.fromUserInput(self.locationEdit.text())
        self.exampleView.load(url)
        self.exampleView.setFocus()
    def go_myHome(self):
        self.exampleView.load(QUrl.fromLocalFile(self.startfilepath))
        self.exampleView.setFocus()

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkYellow)
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns = ["\\bFalse\\b", "\\bNone\\b", "\\bTrue\\b","\\band\\b", "\\bas\\b", "\\bassert\\b",
                "\\bbreak\\b", "\\bclass\\b", "\\bcontinue\\b", "\\bdef\\b",
                "\\bdel\\b", "\\belif\\b", "\\belse\\b", "\\bexcept\\b",
                "\\bfinally\\b", "\\bfor\\b", "\\bfrom\\b",
                "\\bglobal\\b", "\\bif\\b", "\\bimport\\b", "\\bin\\b",
                "\\bis\\b", "\\blambda\\b", "\\bnonlocal\\b",
                "\\bnot\\b", "\\bor\\b", "\\bpass\\b",
                "\\braise\\b", "\\breturn\\b", "\\btry\\b", "\\bwhile\\b",
                "\\bwith\\b", "\\byield\\b"]

        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        commentFormat = QTextCharFormat()
        commentFormat.setFontWeight(QFont.Bold)
        commentFormat.setForeground(Qt.black)
        self.highlightingRules.append((QRegExp("\\b#[^\n]*\\b"),
                commentFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("//[^\n]*"),singleLineCommentFormat))
        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))
        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if len(sys.argv) is 1:
        mainWindow = MainWindow()
    elif len(sys.argv) is 2:
        mainWindow = MainWindow()
        mainWindow.clickAction_exampleDirectOpen(sys.argv[1])
    mainWindow.show()
    import ctypes
    myappid = '파이스터디프로그램' # 반드시 유니코드가 와야됨
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    sys.exit(app.exec_())


