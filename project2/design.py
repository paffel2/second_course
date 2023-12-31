from PyQt5 import QtCore, QtWidgets
from functions import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(26, 90, 291, 52))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.arrayLengthField = QtWidgets.QHBoxLayout()
        self.arrayLengthField.setObjectName("arrayLengthField")
        self.arrayLengthLabel = QtWidgets.QLabel(self.widget)
        self.arrayLengthLabel.setObjectName("arrayLengthLabel")
        self.arrayLengthField.addWidget(self.arrayLengthLabel)
        self.arrayLengthLinedEdit = QtWidgets.QLineEdit(self.widget)
        self.arrayLengthLinedEdit.setObjectName("arrayLengthLinedEdit")
        self.arrayLengthField.addWidget(self.arrayLengthLinedEdit)

        self.verticalLayout.addLayout(self.arrayLengthField)
        self.arrayRangeField = QtWidgets.QHBoxLayout()
        self.arrayRangeField.setObjectName("arrayRangeField")
        self.arrayRangeLabel = QtWidgets.QLabel(self.widget)
        self.arrayRangeLabel.setObjectName("arrayRangeLabel")
        self.arrayRangeField.addWidget(self.arrayRangeLabel)
        self.minValueLineEdit = QtWidgets.QLineEdit(self.widget)
        self.minValueLineEdit.setObjectName("minValueLineEdit")
        self.arrayRangeField.addWidget(self.minValueLineEdit)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.arrayRangeField.addWidget(self.label)
        self.maxValueLineEdit = QtWidgets.QLineEdit(self.widget)
        self.maxValueLineEdit.setObjectName("maxValueLineEdit")
        self.arrayRangeField.addWidget(self.maxValueLineEdit)
        self.verticalLayout.addLayout(self.arrayRangeField)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(510, 70, 211, 83))
        self.widget1.setObjectName("widget1")
        self.actionButtons = QtWidgets.QVBoxLayout(self.widget1)
        self.actionButtons.setContentsMargins(0, 0, 0, 0)
        self.actionButtons.setObjectName("actionButtons")
        self.createArrayButton = QtWidgets.QPushButton(self.widget1)
        self.createArrayButton.setObjectName("createArrayButton")
        self.actionButtons.addWidget(self.createArrayButton)
        self.sortButton = QtWidgets.QPushButton(self.widget1)
        self.sortButton.setEnabled(False)
        self.sortButton.setObjectName("sortButton")
        self.actionButtons.addWidget(self.sortButton)
        self.resetButton = QtWidgets.QPushButton(self.widget1)
        self.resetButton.setEnabled(False)
        self.resetButton.setObjectName("resetButton")
        self.actionButtons.addWidget(self.resetButton)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(40, 180, 691, 351))
        self.widget2.setObjectName("widget2")
        self.tablesLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.tablesLayout.setContentsMargins(0, 0, 0, 0)
        self.tablesLayout.setSpacing(200)
        self.tablesLayout.setObjectName("tablesLayout")
        self.inputTable = QtWidgets.QTableWidget(self.widget2)
        self.inputTable.setEnabled(False)
        self.inputTable.setRowCount(10)
        self.inputTable.setColumnCount(1)
        self.inputTable.setObjectName("inputTable")
        self.inputTable.horizontalHeader().setCascadingSectionResizes(False)
        self.inputTable.horizontalHeader().setDefaultSectionSize(206)
        self.inputTable.setHorizontalHeaderLabels(["Значение"])
        self.tablesLayout.addWidget(self.inputTable)
        self.resultTable = QtWidgets.QTableWidget(self.widget2)
        self.resultTable.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultTable.sizePolicy().hasHeightForWidth())
        self.resultTable.setSizePolicy(sizePolicy)
        self.resultTable.setRowCount(10)
        self.resultTable.setColumnCount(1)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.horizontalHeader().setCascadingSectionResizes(False)
        self.resultTable.horizontalHeader().setDefaultSectionSize(206)
        self.resultTable.setHorizontalHeaderLabels(["Значение"])
        self.tablesLayout.addWidget(self.resultTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.array = []
        self.minArrayValue = 0
        self.maxArrayValue = 0
        self.arraySizeValue = 1
        self.defaultCountRows = 10

        self.defaultArraySizeTextValue = "2"
        self.defaultMinArrayValueTextValue = "1"
        self.defaultMaxArrayValueTextValue = "10"

        #actions
        self.createArrayButton.clicked.connect(self.createArray)
        self.resetButton.clicked.connect(self.resetAction)
        self.sortButton.clicked.connect(self.sortAction)

        #default values
        self.arrayLengthLinedEdit.setText(self.defaultArraySizeTextValue)
        self.minValueLineEdit.setText(self.defaultMinArrayValueTextValue)
        self.maxValueLineEdit.setText(self.defaultMaxArrayValueTextValue)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сортировка массива"))
        self.arrayLengthLabel.setText(_translate("MainWindow", "Длина массива"))
        self.arrayRangeLabel.setText(_translate("MainWindow", "Диапазон значений от"))
        self.label.setText(_translate("MainWindow", "до"))
        self.createArrayButton.setText(_translate("MainWindow", "Создать массив"))
        self.sortButton.setText(_translate("MainWindow", "Сортировать массив"))
        self.resetButton.setText(_translate("MainWindow", "Очистить данные"))
    
    def send_error(self,message):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setText(message)
            msg_box.setWindowTitle("Ошибка")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg_box.exec()

    def createArray(self):
        arraySize = self.arrayLengthLinedEdit.text()
        minArrayValue = self.minValueLineEdit.text()
        maxArrayValue = self.maxValueLineEdit.text()
        if not checkInt(arraySize) or int(arraySize) < 0:
            self.arrayLengthLinedEdit.setText('')
            self.send_error('Неверно задан размер массива')
        elif not checkFloat(minArrayValue):
            self.minValueLineEdit.setText('')
            self.send_error('Неверно задана нижняя граница массива')
        elif not checkFloat(maxArrayValue):
            self.maxValueLineEdit.setText('')
            self.send_error('Неверно задана верхняя граница массива')
        elif float(minArrayValue)  > float(maxArrayValue):
            self.maxValueLineEdit.setText('')
            self.minValueLineEdit.setText('')
            self.send_error('Верхняя граница массива меньше нижней')
        else:
            self.sortButton.setEnabled(True)
            self.resetButton.setEnabled(True)
            self.createArrayButton.setEnabled(False)
            self.arraySizeValue = int(arraySize)
            self.minArrayValue = float(minArrayValue)
            self.maxArrayValue = float(maxArrayValue)
            self.inputTable.setRowCount(self.arraySizeValue)
            self.resultTable.setRowCount(self.arraySizeValue)
            self.inputTable.setEnabled(True)
            self.arrayLengthLinedEdit.setEnabled(False)
            self.minValueLineEdit.setEnabled(False)
            self.maxValueLineEdit.setEnabled(False)
    
    def resetAction(self):

        self.arrayLengthLinedEdit.setText(self.defaultArraySizeTextValue)
        self.minValueLineEdit.setText(self.defaultMinArrayValueTextValue)
        self.maxValueLineEdit.setText(self.defaultMaxArrayValueTextValue)
        self.inputTable.setRowCount(0)
        self.resultTable.setRowCount(0)
        self.inputTable.setRowCount(self.defaultCountRows)
        self.resultTable.setRowCount(self.defaultCountRows)
        self.sortButton.setEnabled(False)
        self.resetButton.setEnabled(False)
        self.createArrayButton.setEnabled(True)
        self.inputTable.setEnabled(False)
        self.resultTable.setEnabled(False)
        self.arrayLengthLinedEdit.setEnabled(True)
        self.minValueLineEdit.setEnabled(True)
        self.maxValueLineEdit.setEnabled(True)
    
    # Получение исходного массива из таблицы
    def getArray(self):
        tempArray = []       
        for i in range(0,self.arraySizeValue):
            tempValue = self.inputTable.item(i,0).text()
            if not checkFloat(tempValue):
                self.send_error("Неверное значение внутри массива " + str(i+1))
                self.inputTable.setItem(i,0,QtWidgets.QTableWidgetItem(''))
                tempArray = []
                break
            elif not (self.minArrayValue <= float(tempValue) <= self.maxArrayValue):
                self.send_error("Неверное значение внутри массива " + str(i+1))
                self.inputTable.setItem(i,0,QtWidgets.QTableWidgetItem(''))
                tempArray = []
                break
            else:
                tempArray.append(float(tempValue))
        if len(tempArray) == 0:
            return False
        else:
            self.array = tempArray
            return True
        
    # Сортировка исходного массива и вывод в таблицу результатов
    def sortAction(self):
        readArrayFlag = self.getArray()
        if readArrayFlag:
            sortedArray = cocktailSort(self.array)
            for i in range(0,self.arraySizeValue):
                self.resultTable.setItem(i,0,QtWidgets.QTableWidgetItem(str(sortedArray[i])))
            self.resultTable.setEnabled(True)
            self.sortButton.setEnabled(False)
        

