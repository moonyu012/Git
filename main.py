import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.btn1=QPushButton("Message", self)
        self.btn1.clicked.connect(self.activateMessage)

        vbox=QVBoxLayout() # 수직 레이아웃 위젯 생성 코드
        vbox.addStretch(1) # 빈공간 생성 코드
        vbox.addWidget(self.btn1) # 버튼 위치
        vbox.addStretch(1) # 빈공간 생성 코드

        self.setLayout(vbox) # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

    def activateMessage(self): # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        QMessageBox.information(self, 'Information', '메시지를 적을 수 있는 상자입니다!')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())