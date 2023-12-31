from PyQt5 import QtCore, QtWidgets
from textclass import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(820, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 90, 761, 391))
        self.widget.setObjectName("widget")
        self.textFields = QtWidgets.QHBoxLayout(self.widget)
        self.textFields.setContentsMargins(0, 0, 0, 0)
        self.textFields.setObjectName("textFields")
        self.inputField = QtWidgets.QVBoxLayout()
        self.inputField.setObjectName("inputField")
        self.inputLabel = QtWidgets.QLabel(self.widget)
        self.inputLabel.setObjectName("inputLabel")
        self.inputField.addWidget(self.inputLabel)
        self.inputTextEdit = QtWidgets.QTextEdit(self.widget)
        self.inputTextEdit.setObjectName("inputTextEdit")
        self.inputField.addWidget(self.inputTextEdit)
        self.textFields.addLayout(self.inputField)
        self.outputField = QtWidgets.QVBoxLayout()
        self.outputField.setObjectName("outputField")
        self.outputLabel = QtWidgets.QLabel(self.widget)
        self.outputLabel.setObjectName("outputLabel")
        self.outputField.addWidget(self.outputLabel)
        self.outputTextEdit = QtWidgets.QTextEdit(self.widget)
        self.outputTextEdit.setObjectName("outputTextEdit")
        self.outputTextEdit.setEnabled(False)
        self.outputField.addWidget(self.outputTextEdit)
        self.textFields.addLayout(self.outputField)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 40, 681, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.taskNameLabel = QtWidgets.QLabel(self.widget1)
        self.taskNameLabel.setObjectName("taskNameLabel")
        self.horizontalLayout_2.addWidget(self.taskNameLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.countWordsButton = QtWidgets.QPushButton(self.widget1)
        self.countWordsButton.setObjectName("countWordsButton")
        self.horizontalLayout.addWidget(self.countWordsButton)
        self.resetButton = QtWidgets.QPushButton(self.widget1)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.resetButton.clicked.connect(self.resetAction)
        self.countWordsButton.clicked.connect(self.findWords)

        self.inputTextEdit.setText('''Но притворитесь! Этот взгляд
Всё может выразить так чудно!
Ах, обмануть меня не трудно!..
Я сам обманываться рад!''')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск слов"))
        self.inputLabel.setText(_translate("MainWindow", "Исходный текст"))
        self.outputLabel.setText(_translate("MainWindow", "Найденные слова"))
        self.taskNameLabel.setText(_translate("MainWindow", "Задание: Найти все слова в тексте, оканчивающиеся на гласную букву."))
        self.countWordsButton.setText(_translate("MainWindow", "Найти слова"))
        self.resetButton.setText(_translate("MainWindow", "Повторить"))
    
    # Поиск слов
    def findWords(self):
        self.countWordsButton.setEnabled(False)
        tempText = self.inputTextEdit.toPlainText()
        self.inputTextEdit.setEnabled(False)
        textObject = Text(tempText)
        result = textObject.findWords()
        self.outputTextEdit.setEnabled(True)
        self.outputTextEdit.setText(', '.join(result))
        self.resetButton.setEnabled(True)
    
    def resetAction(self):
        self.countWordsButton.setEnabled(True)
        self.resetButton.setEnabled(False)
        self.outputTextEdit.setEnabled(False)
        self.outputTextEdit.setText('')
        self.inputTextEdit.setEnabled(True)
        self.inputTextEdit.setText('')