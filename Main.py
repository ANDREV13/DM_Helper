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
    this_label = 0
    this_label_name = ''
    t1 = []

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
            self.lenn = len(self.strss)
        else:
            self.strss = [self.strs]
            self.lenn = 0
        q = 0
        for i in self.strss[self.t]:
            self.buttons.append(QPushButton(self))
            self.buttons[q].resize(170, 100)
            self.buttons[q].move(0, 0+(q*100))
            self.buttons[q].setText(str(i))
            self.t1.append(0)
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
        self.label_forward.clicked.connect(self.lab_forw)
        self.label_back = QPushButton(self)
        self.label_back.setText('<=')
        self.label_back.resize(85, 85)
        self.label_back.move(170, 650)
        self.label_back.clicked.connect(self.lab_bk)

        self.show()

    def run(self, z = 0, t = 0, a = '1'):
        if a == '1':
            writing = self.sender().text()
            self.t1[self.this_label] = 0
        else:
            writing = a
        for i in self.disp:
            i.setText('')
        if isinstance(self.strs[writing], list):
            self.string = self.strs[writing][t]
            self.this_label_name = writing
        else:
            self.string = self.strs[writing]
            self.this_label_name = writing
        self.str1 = ''
        self.count = 0
        self.this_label = z
        for i in str(self.string):
            self.str1 += i
            if len(self.str1) > 45:
                self.count += 1
                self.str1 = ''
            self.disp[self.count].setText(self.str1)

    def cut(self, lis, listt=[]):
        lis1 = {}
        liss = []
        lisq = {}
        for i in lis:
            lisq[i] = lis[i]
        j = 0
        for i in lis:
            if j < 6:
                lis1[i] = lis[i]
                del lisq[i]
            j += 1
        listt.append(lis1)
        if len(lisq) > 6:
            return self.cut(lisq, listt)
        else:
            listt.append(lisq)
            return listt

    def but_forw(self):
        if self.t < self.lenn-1:
            self.t += 1
            q = 0
            for i in self.strss[self.t]:
                self.buttons[q].show()
                self.buttons[q].setText(str(i))
                q += 1
            for i in range(q, len(self.buttons)):
                self.buttons[q].hide()
                q += 1

    def but_bk(self):
        if self.t > 0:
            self.t -= 1
            q = 0
            for i in self.strss[self.t]:
                self.buttons[q].show()
                self.buttons[q].setText(str(i))
                q += 1
            for i in range(q, len(self.buttons)):
                self.buttons[q].hide()
                q += 1

    def lab_forw(self):
        if isinstance(self.strs[self.this_label_name], list):
            if self.t1[self.this_label] < len(self.strs[self.this_label_name])-1:
                self.t1[self.this_label] += 1
                self.run(self.this_label, self.t1[self.this_label], self.this_label_name)

    def lab_bk(self):
        if isinstance(self.strs[self.this_label_name], list):
            if self.t1[self.this_label] > 0:
                self.t1[self.this_label] -= 1
                self.run(self.this_label, self.t1[self.this_label], self.this_label_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainProject({'test1': 'test'*50, 'test2': ['test'*55, 'test'*100], 'test3': 'test'*200, 'test4': ['test',
                      'test'*2, 'test'*3, 'test'*4], 'test5': 'test', 'test6': '--', 'test7': 'test'})
    sys.exit(app.exec_())
