__author__ = 'KHS-1'
import sys
import os
import codecs
import binascii
from PyQt5.QtCore import QFile, QIODevice, QTextStream, QProcess, QUrl
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QInputDialog,QMainWindow, QMessageBox, QWidget)

from ui_PyPreviewer import Ui_MainWindow



class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #self.centralWidget = PyPreviewer(self)
        #self.setCentralWidget(self.centralWidget)

        #메뉴 이벤트 생성
        self.createEvent()

        self.dirty = False
        self.plainTextEdit_2.textChanged.connect(self.setDirty)

        self.fileName = None

        self.exampleView.load(QUrl("http://www.google.com"))

        #사용자 입력 파이썬 파일 실행
        print ('Connecting process')
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)
        self.process.started.connect(lambda: print('ExampleProgramStarted!'))
        self.process.finished.connect(lambda:print('ExampleProgramFinished!'))
        print('Starting process')
        #self.process.start('python', ['ExampleTest.py'])

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
    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self)
        if fileName:
            fd = QFile(fileName)
            if not fd.open(QIODevice.ReadOnly):
                QMessageBox.information(self, "Unable to open file",fd.errorString())
                return

            output = QTextStream(fd).readAll()

            # Display contents.
            self.centralWidget.plainTextEdit.setPlainText(output)
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
            print(fname)
            #self.exampleView.load(QUrl(fname))
            self.exampleView.setUrl(QUrl.fromLocalFile(fname))
            #self.plainTextEdit_2.setPlainText(codecs.open(fname, "r", "utf-8" ).read())
            #self.fileName = fname
        else:
            return
        self.updateStatus('example File opened.')


    def clickAction_fileNew(self):
        #'''Clear the editor window for a new file with name specified in fileSaveAs method.'''
        self.plainTextEdit_2.clear()
        self.statusBar().showMessage('새 소스파일 생성', 8000)


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
        self.process.start('python', [self.fileName])
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
        print(text.strip())
        self.append_plainTextEdit_3(text)

    def stderrReady(self):
        text = str(self.process.readAllStandardError(), "utf-8")
        print(text.strip())
        self.append_plainTextEdit_3(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


