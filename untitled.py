import sys
from random import randint

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator, QKeySequence, QShortcut

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.game = Game()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(360, 300))
        MainWindow.setMaximumSize(QtCore.QSize(360, 300))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)

        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        
        self.hintLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.hintLine.setGeometry(QtCore.QRect(0, 40, 360, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.hintLine.setFont(font)
        self.hintLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hintLine.setObjectName("hintLine")

        
        self.checkButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.checkButton.setGeometry(QtCore.QRect(170, 210, 140, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.checkButton.setFont(font)
        self.checkButton.setObjectName("checkButton")
        self.checkButton.clicked.connect(self.run_game)
        

        self.InputLine = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.InputLine.setGeometry(QtCore.QRect(50, 210, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.InputLine.setFont(font)
        self.InputLine.setText("")
        self.InputLine.setMaxLength(2)
        self.InputLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputLine.setObjectName("InputLine")
        int_validator = QIntValidator(0, 99)
        self.InputLine.setValidator(int_validator)
        
        
        self.outputLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.outputLine.setGeometry(QtCore.QRect(0, 90, 360, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.outputLine.setFont(font)
        self.outputLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.outputLine.setObjectName("outputLine")
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NumGame"))
        self.hintLine.setText(_translate("MainWindow", "Загаданно число от 0 до 100."))
        self.checkButton.setText(_translate("MainWindow", "Угадал?"))
        self.outputLine.setText(_translate("MainWindow", "У тебя 5 попыток отгадать."))
        
        
    def run_game(self):

        if self.InputLine.text() != '':
            
            if self.game.finished == True:
                self.game.random = randint(0, 99)
                self.game.stage = 1
                self.InputLine.setDisabled(False)
                self.hintLine.setText("Загадано число от 0 до 100.")
                self.checkButton.setText("Угадал?")
                self.outputLine.setText("У тебя 5 попыток отгадать.")
                self.game.finished = False
                return

            input_num = int(self.InputLine.text())
            
            
            if self.game.game_stage() == 5 and input_num != self.game.random:
                self.hintLine.setText('Ты проиграл!')
                self.outputLine.setText(f'Загадано было число {self.game.random}.')  
                self.checkButton.setText('Заново')
                self.InputLine.clear()
                self.InputLine.setDisabled(True)
                self.game.finished = True
                return

            if input_num == self.game.random and self.game.game_stage() <= 5:
                self.hintLine.setText('Угадал!')
                self.outputLine.setText('Поздравляю!')
                self.checkButton.setText('Заново')
                self.InputLine.clear()
                self.InputLine.setDisabled(True)
                self.game.finished = True
                return

            else:
                if input_num < self.game.random and self.game.game_stage() <= 5:
                    self.hintLine.setText('Нет, загаданное число больше.')
                elif input_num > self.game.random and self.game.game_stage() <= 5:
                    self.hintLine.setText('Нет, загаданное число меньше.')
                self.outputLine.setText(f'Уже {5 - self.game.stage}.')
                self.game.stage += 1  
                self.InputLine.clear()
                return
        

class Game:
    def __init__(self):
        self.finished = False
        self.random = randint(0, 99)
        self.stage = 1

    def game_stage(self) -> int:
        return self.stage



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
