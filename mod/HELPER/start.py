import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        btn1 = QPushButton("1. Variable 변수", self)
        btn1.move(90, 20)

        btn2 = QPushButton("2. Datatype 자료형", self)
        btn2.move(90, 50)

        btn3 = QPushButton("3. String 문자열", self)
        btn3.move(90, 80)

        btn4 = QPushButton("4. List 리스트", self)
        btn4.move(90, 110)

        btn5 = QPushButton("5. Tuple 튜플", self)
        btn5.move(90, 140)

        btn6 = QPushButton("6. Dictionary 사전", self)
        btn6.move(90, 170)

        btn7 = QPushButton("7. Bool 부울", self)
        btn7.move(90, 200)

        btn8 = QPushButton("8. If 조건문", self)
        btn8.move(90, 230)

        btn9 = QPushButton("9. Loop 반복문", self)
        btn9.move(90, 260)

        btn10 = QPushButton("10. Function 함수", self)
        btn10.move(90, 290)

        btn11 = QPushButton("11. Class 클래스", self)
        btn11.move(90, 320)

        btn12 = QPushButton("12. Con 생성자/소멸자", self)
        btn12.move(90, 350)

        btn13 = QPushButton("13. Inherit 상속", self)
        btn13.move(90, 380)

        btn14 = QPushButton("14. Overloading 오버로딩", self)
        btn14.move(90, 410)

        btn15 = QPushButton("15. Module 모듈", self)
        btn15.move(90, 440)

        btn16 = QPushButton("16. I/O 입출력", self)
        btn16.move(90, 470)

        btn17 = QPushButton("17. Exception 예외처리", self)
        btn17.move(90, 500)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)
        btn4.clicked.connect(self.buttonClicked)
        btn5.clicked.connect(self.buttonClicked)
        btn6.clicked.connect(self.buttonClicked)
        btn7.clicked.connect(self.buttonClicked)
        btn8.clicked.connect(self.buttonClicked)
        btn9.clicked.connect(self.buttonClicked)
        btn10.clicked.connect(self.buttonClicked)
        btn11.clicked.connect(self.buttonClicked)
        btn12.clicked.connect(self.buttonClicked)
        btn13.clicked.connect(self.buttonClicked)
        btn14.clicked.connect(self.buttonClicked)
        btn15.clicked.connect(self.buttonClicked)
        btn16.clicked.connect(self.buttonClicked)
        btn17.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(800, 100, 290, 550)
        self.setWindowTitle('HELPER')
        self.show()


    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
