import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QColor


class MainProject(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.strs = ['111111111111111111111111111111111111111111111111111111', '22', '33', '44', '55', '66', '77', '88']
        self.setGeometry(200, 150, 600, 1200)
        self.setWindowTitle('DMHelper')
        self.buttons = []
        self.buttons_forward = QPushButton(self)
        self.buttons_forward.setText('=>')
        self.buttons_forward.resize(85, 85)
        self.buttons_forward.move(85, 700)
        self.buttons_back = QPushButton(self)
        self.buttons_back.setText('<=')
        self.buttons_back.resize(85, 85)
        self.buttons_back.move(0, 700)

        for i in range(7):
            self.buttons.append(QPushButton(self))
            self.buttons[i].resize(170, 100)
            self.buttons[i].move(0, 0+(i*100))
            self.buttons[i].setText(str(i))
            self.buttons[i].clicked.connect(self.run)

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
        self.string = self.strs[int(self.sender().text())]
        self.str1 = ''
        self.count = 0
        for i in self.string:
            self.str1 += i
            if len(self.str1) > 45:
                self.count += 1

                self.str1 = ''
            self.disp[self.count].setText(self.str1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainProject()
    sys.exit(app.exec_())