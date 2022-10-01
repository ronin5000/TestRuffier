from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *
 
     
class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
    
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
    
        # создаём и настраиваем графические элементы:
        self.initUI()
    
        #устанавливает связи между элементами
        self.connects()
    
        # старт:
        self.show()
    
    def initUI(self):
        ''' создаёт графические элементы '''
        self.bin_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.layont_line = QVBoxLayout()
        self.layont_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layont_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layont_line.addWidget(self.bin_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layont_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.bin_next.clicked.connect(self.next_click)
    
    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
app = QApplication([])
mw = MainWin()
app.exec_()
 
