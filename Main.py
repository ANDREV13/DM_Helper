import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QColor


class MainProject(QWidget):

    def __init__(self, strs):
        super().__init__()
        self.initUI(strs)


    def initUI(self, strs):
        self.strs = strs
        self.setGeometry(200, 150, 600, 1200)
        self.setWindowTitle('DMHelper')
        self.buttons = []
        self.buttons_forward = QPushButton(self)
        self.buttons_forward.setText('=>')
        self.buttons_forward.resize(85, 85)
        self.buttons_forward.move(85, 700)
        self.buttons_forward.clicked.connect(self.but_forw)
        self.buttons_back = QPushButton(self)
        self.buttons_back.setText('<=')
        self.buttons_back.resize(85, 85)
        self.buttons_back.move(0, 700)
        self.buttons_back.clicked.connect(self.but_bk)

        self.t = 0
        self.strss = []
        if len(self.strs) > 6:
            self.strss = self.cut(self.strs)
            self.len = len(self.strss)
        else:
            self.strss = [self.strs]
            self.lenn = 0
        q = 0
        for i in self.strss[self.t]:
            self.buttons.append(QPushButton(self))
            self.buttons[q].resize(170, 100)
            self.buttons[q].move(0, 0+(q*100))
            self.buttons[q].setText(i)
            self.buttons[q].clicked.connect(self.run)
            q+=1

        self.disp = []
        for i in range(30):
            self.disp.append(QLabel(self))
            self.disp[i].resize(400, 20)
            self.disp[i].move(180, 10 + (20*i))

        self.label_forward = QPushButton(self)
        self.label_forward.setText('=>')
        self.label_forward.resize(85, 85)
        self.label_forward.move(515, 650)
        self.label_back = QPushButton(self)
        self.label_back.setText('<=')
        self.label_back.resize(85, 85)
        self.label_back.move(170, 650)

        self.show()

    def run(self):
        for i in self.disp:
            i.setText('')
        self.string = self.strs[self.sender().text()]
        self.str1 = ''
        self.count = 0
        for i in str(self.string):
            self.str1 += i
            if len(self.str1) > 45:
                self.count += 1

                self.str1 = ''
            self.disp[self.count].setText(self.str1)

    def cut(self, lis, listt=[]):
        lis1 = {}
        liss = []
        for i in range(6):
            lis1[i] = lis[i]
            del lis[i]
        listt.append(lis1)
        if len(lis) > 6:
            return self.cut(lis, listt)
        else:
            listt.append(lis)
            return listt

    def but_forw(self):
        if self.t < self.lenn-1:
            self.t += 1
            q = 0
            for i in self.strss[self.t]:
                self.buttons[q] = QPushButton(self)
                self.buttons[q].resize(170, 100)
                self.buttons[q].move(0, 0 + (q * 100))
                self.buttons[q].setText(i)
                self.buttons[q].clicked.connect(self.run)

    def but_bk(self):
        if self.t > 0:
            self.t -= 1
            for i in self.strss[self.t]:
                self.buttons[i] = QPushButton(self)
                self.buttons[i].resize(170, 100)
                self.buttons[i].move(0, 0 + (i * 100))
                self.buttons[i].setText(i)
                self.buttons[i].clicked.connect(self.run)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainProject({'11': '11', 'aaa': 'aaaaaaaaaaaaaaa', 'aswss': 111})
    sys.exit(app.exec_())