from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from functions import *
from kineticconst import *


# Класс для отрисовки графика
class Canvas(FigureCanvas):
    def __init__(self, parent=None, xs=[], ys=[], title="", xname="", yname=""):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel(xname)
        self.axes.set_ylabel(yname)
        self.axes.set_title(title)
        super(Canvas, self).__init__(fig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 900)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputDataFrame = QtWidgets.QGroupBox(self.centralwidget)
        self.inputDataFrame.setGeometry(QtCore.QRect(10, 60, 261, 431))
        self.inputDataFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputDataFrame.setAutoFillBackground(False)
        self.inputDataFrame.setStyleSheet("QGroupBox { border: 4px double gray;}")
        self.inputDataFrame.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.inputDataFrame.setFlat(False)
        self.inputDataFrame.setCheckable(False)
        self.inputDataFrame.setObjectName("inputDataFrame")
        self.widget = QtWidgets.QWidget(self.inputDataFrame)
        self.widget.setGeometry(QtCore.QRect(20, 40, 221, 307))
        self.widget.setObjectName("widget")
        self.inputLayout = QtWidgets.QVBoxLayout(self.widget)
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLayout.setObjectName("inputLayout")
        self.concSubstanceBLayout = QtWidgets.QHBoxLayout()
        self.concSubstanceBLayout.setObjectName("concSubstanceBLayout")
        self.concSubstanceBLabel = QtWidgets.QLabel(self.widget)
        self.concSubstanceBLabel.setAutoFillBackground(False)
        self.concSubstanceBLabel.setStyleSheet("color: green")
        self.concSubstanceBLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.concSubstanceBLabel.setLineWidth(0)
        self.concSubstanceBLabel.setObjectName("concSubstanceBLabel")
        self.concSubstanceBLayout.addWidget(self.concSubstanceBLabel)
        self.concSubstanceBLineEdit = QtWidgets.QLineEdit(self.widget)
        self.concSubstanceBLineEdit.setObjectName("concSubstanceBLineEdit")
        self.concSubstanceBLayout.addWidget(self.concSubstanceBLineEdit)
        self.inputLayout.addLayout(self.concSubstanceBLayout)
        self.concSubstanceCLayout = QtWidgets.QHBoxLayout()
        self.concSubstanceCLayout.setObjectName("concSubstanceCLayout")
        self.concSubstanceCLabel = QtWidgets.QLabel(self.widget)
        self.concSubstanceCLabel.setStyleSheet("color: red")
        self.concSubstanceCLabel.setObjectName("concSubstanceCLabel")
        self.concSubstanceCLayout.addWidget(self.concSubstanceCLabel)
        self.concSubstanceCLineEdit = QtWidgets.QLineEdit(self.widget)
        self.concSubstanceCLineEdit.setObjectName("concSubstanceCLineEdit")
        self.concSubstanceCLayout.addWidget(self.concSubstanceCLineEdit)
        self.inputLayout.addLayout(self.concSubstanceCLayout)
        self.numOfDotsLayout = QtWidgets.QHBoxLayout()
        self.numOfDotsLayout.setObjectName("numOfDotsLayout")
        self.numOfDotsLabel = QtWidgets.QLabel(self.widget)
        self.numOfDotsLabel.setObjectName("numOfDotsLabel")
        self.numOfDotsLayout.addWidget(self.numOfDotsLabel)
        self.numOfDotsSpinBox = QtWidgets.QSpinBox(self.widget)
        self.numOfDotsSpinBox.setMinimum(2)
        self.numOfDotsSpinBox.setObjectName("numOfDotsSpinBox")
        self.numOfDotsLayout.addWidget(self.numOfDotsSpinBox)
        self.inputLayout.addLayout(self.numOfDotsLayout)
        self.dotsTable = QtWidgets.QTableWidget(self.widget)
        self.dotsTable.setAlternatingRowColors(True)
        self.dotsTable.setRowCount(2)
        self.dotsTable.setColumnCount(2)
        self.dotsTable.setObjectName("dotsTable")
        self.dotsTable.horizontalHeader().setVisible(True)
        self.dotsTable.setHorizontalHeaderLabels(["Ca, моль/л", "t, c"])
        self.inputLayout.addWidget(self.dotsTable)
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setSpacing(20)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.countButton = QtWidgets.QPushButton(self.widget)
        self.countButton.setObjectName("countButton")
        self.buttonsLayout.addWidget(self.countButton)
        self.resetButton = QtWidgets.QPushButton(self.widget)
        self.resetButton.setObjectName("resetButton")
        self.buttonsLayout.addWidget(self.resetButton)
        self.inputLayout.addLayout(self.buttonsLayout)

        # заполнение виджета с графиком
        self.canvas = self.createCanvas()
        self.canvas_layout = QtWidgets.QVBoxLayout()
        self.canvas_layout.addWidget(self.canvas)
        self.frameForGraphicWidget = QtWidgets.QWidget(self.centralwidget)
        self.frameForGraphicWidget.setGeometry(QtCore.QRect(310, 80, 580, 580))
        self.frameForGraphicWidget.setStyleSheet("border: 1px solid black;")
        self.frameForGraphicWidget.setObjectName("frameForGraphicWidget")
        self.frameForGraphicWidget.setLayout(self.canvas_layout)

        # actions
        self.numOfDotsSpinBox.textChanged.connect(self.changeNumOfRows)
        self.resetButton.clicked.connect(self.resetAction)
        self.countButton.clicked.connect(self.countAction)

        self.dotsTable.setRowCount(8)
        self.dotsTable.setColumnCount(2)
        self.numOfDotsSpinBox.setValue(8)
        self.concSubstanceBLineEdit.setText("0.8")
        self.concSubstanceCLineEdit.setText("1.5")

        self.dotsTable.setItem(0, 0, QtWidgets.QTableWidgetItem("2.2"))
        self.dotsTable.setItem(1, 0, QtWidgets.QTableWidgetItem("1.7"))
        self.dotsTable.setItem(2, 0, QtWidgets.QTableWidgetItem("1.5"))
        self.dotsTable.setItem(3, 0, QtWidgets.QTableWidgetItem("1.2"))
        self.dotsTable.setItem(4, 0, QtWidgets.QTableWidgetItem("1.1"))
        self.dotsTable.setItem(5, 0, QtWidgets.QTableWidgetItem("1.0"))
        self.dotsTable.setItem(6, 0, QtWidgets.QTableWidgetItem("0.9"))
        self.dotsTable.setItem(7, 0, QtWidgets.QTableWidgetItem("0.8"))

        self.dotsTable.setItem(0, 1, QtWidgets.QTableWidgetItem("0"))
        self.dotsTable.setItem(1, 1, QtWidgets.QTableWidgetItem("1.7"))
        self.dotsTable.setItem(2, 1, QtWidgets.QTableWidgetItem("2.5"))
        self.dotsTable.setItem(3, 1, QtWidgets.QTableWidgetItem("3.4"))
        self.dotsTable.setItem(4, 1, QtWidgets.QTableWidgetItem("4"))
        self.dotsTable.setItem(5, 1, QtWidgets.QTableWidgetItem("4.6"))
        self.dotsTable.setItem(6, 1, QtWidgets.QTableWidgetItem("5.2"))
        self.dotsTable.setItem(7, 1, QtWidgets.QTableWidgetItem("6"))

        self.resultTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.resultTableWidget.setObjectName("resultTableWidget")
        self.resultTableWidget.setGeometry(QtCore.QRect(20, 680, 871, 192))
        self.resultTableWidget.setRowCount(0)
        self.resultTableWidget.setColumnCount(5)
        self.resultTableWidget.setAlternatingRowColors(True)
        self.resultTableWidget.setObjectName("resultTable")
        self.resultTableWidget.horizontalHeader().setVisible(True)
        self.resultTableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )
        self.resultTableWidget.setHorizontalHeaderLabels(
            ["t, c", "Ca Эксп, моль/л", "Ca, моль/л", "Cb, моль/л", "Cc, моль/л"]
        )
        self.resultTableWidget.setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Оценка кинетических констант")
        )
        self.inputDataFrame.setTitle(_translate("MainWindow", "Ввод данных"))
        self.concSubstanceBLabel.setText(
            _translate("MainWindow", "Консентрация Cb, моль/л")
        )
        self.concSubstanceCLabel.setText(
            _translate("MainWindow", "Концентрация Cc, моль/л")
        )
        self.numOfDotsLabel.setText(_translate("MainWindow", "Количество точек"))
        self.countButton.setText(_translate("MainWindow", "Вычислить"))
        self.resetButton.setText(_translate("MainWindow", "Очистить"))

    def changeNumOfRows(self):
        n = self.numOfDotsSpinBox.text()
        self.dotsTable.setRowCount(int(n))

    def createCanvas(self):
        return Canvas(
            self,
            xname="Время (c)",
            yname="Концентрация (моль/л)",
            title="Экспериментальные точки и апроксимационная кривая",
        )

    def resetAction(self):
        self.concSubstanceBLineEdit.setText("")
        self.concSubstanceCLineEdit.setText("")
        self.dotsTable.setRowCount(0)
        self.dotsTable.setRowCount(2)
        self.numOfDotsSpinBox.setValue(2)
        self.canvas.axes.clear()
        self.canvas_layout.removeWidget(self.canvas)
        self.canvas = self.createCanvas()
        self.canvas_layout.addWidget(self.canvas)
        self.canvas.draw()
        self.resultTableWidget.setRowCount(0)
        self.resultTableWidget.setVisible(False)

    def send_error(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec()

    def countAction(self):
        try:
            self.canvas_layout.removeWidget(self.canvas)
            self.canvas = self.createCanvas()
            self.canvas_layout.addWidget(self.canvas)
            self.canvas.draw()
            self.readConCb()
            self.readConCc()
            self.readListRange()

            self.tList = []
            self.cList = []
            for i in range(0, self.n):
                cTextValue = self.dotsTable.item(i, 0).text()
                tTextValue = self.dotsTable.item(i, 1).text()
                cTempValue = toFloatTableValue(
                    cTextValue,
                    "Неверное значение концентрации элемент №" + str(i + 1),
                    i,
                    0,
                )
                tTempValue = toFloatTableValue(
                    tTextValue, "Неверное значение времени элемент №" + str(i + 1), i, 1
                )
                self.tList.append(tTempValue)
                self.cList.append(cTempValue)

            checkTimeList(self.tList)
            checkConcList(self.cList)

            kineticConstObj = KineticConst(
                self.cb, self.cc, self.cList, self.tList, self.n
            )
            kineticConstObj.countKineticParameters()

            dispertionObj = Dispertion(
                self.cList[0],
                self.tList,
                kineticConstObj.n,
                kineticConstObj.k,
                self.cList,
                self.n,
                self.cb,
                self.cc,
            )

            dispertionObj.countCValues()
            d = dispertionObj.countDispertion()

            self.canvas.axes.plot(
                self.tList, self.cList, color="g", label="Ca Эксп", marker="o"
            )
            self.canvas.axes.plot(
                self.tList,
                dispertionObj.caValuesCounted,
                color="y",
                label="Ca теор.",
                marker="o",
            )
            self.canvas.axes.plot(
                self.tList, dispertionObj.cbValues, color="r", label="Cb", marker="o"
            )
            self.canvas.axes.plot(
                self.tList, dispertionObj.ccValues, color="b", label="Cc", marker="o"
            )
            self.canvas.axes.legend()
            self.canvas.axes.grid(True)
            self.canvas.draw()

            self.resultTableWidget.setRowCount(self.n)
            self.resultTableWidget.setVisible(True)
            for i in range(self.n):
                self.resultTableWidget.setItem(
                    i, 0, QtWidgets.QTableWidgetItem(str(round(self.tList[i], 2)))
                )
                self.resultTableWidget.setItem(
                    i, 1, QtWidgets.QTableWidgetItem(str(round(self.cList[i], 2)))
                )
                self.resultTableWidget.setItem(
                    i,
                    2,
                    QtWidgets.QTableWidgetItem(
                        str(round(dispertionObj.caValuesCounted[i], 2))
                    ),
                )
                self.resultTableWidget.setItem(
                    i,
                    3,
                    QtWidgets.QTableWidgetItem(
                        str(round(dispertionObj.cbValues[i], 2))
                    ),
                )
                self.resultTableWidget.setItem(
                    i,
                    4,
                    QtWidgets.QTableWidgetItem(
                        str(round(dispertionObj.ccValues[i], 2))
                    ),
                )

            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText(
                f"Порядок реакции: {kineticConstObj.n:.3f}\n"
                f"Константа скорости: {kineticConstObj.k:.3f} с{chr(0x207B)}{chr(0x00B9)}\n"
                f"Коэффициент корелляции: {kineticConstObj.r:.3f} \n"
                f"Дисперсия: {d:.3f} (моль\\л){chr(0x00B2)}"
            )
            msg_box.setWindowTitle("Результаты расчета")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg_box.exec()

        except WrongCbValue as e:
            self.send_error(e.message)
            self.concSubstanceBLineEdit.setText("")

        except ValueError as e:
            self.send_error("При расчете параметров возникла ошибка проверьте данные.")

        except WrongCaValue as e:
            self.send_error(e.message)

        except WrongCcValue as e:
            self.send_error(e.message)
            self.concSubstanceBLineEdit.setText("")

        except WrongTableValue as e:
            self.send_error(e.message)
            self.dotsTable.setItem(
                e.row, e.col, QtWidgets.QtWidgets.QTableWidgetItem("")
            )

        except IsNotSortedInAsc as e:
            self.send_error(e.message)
            self.dotsTable.selectRow(e.position)

        except WrongNeighboringValues as e:
            self.send_error(e.message)
            self.dotsTable.selectRow(e.position)

        except TimeNegativeValue as e:
            self.send_error(e.message)
            self.dotsTable.selectRow(e.position)

        except ConcNegativeValue as e:
            self.send_error(e.message)
            self.dotsTable.selectRow(e.position)

    def readConCb(self):
        a = self.concSubstanceBLineEdit.text()
        self.cb = toFloat(a, "Неверное значение концентрации вещества B", WrongCbValue)

    def readConCc(self):
        a = self.concSubstanceCLineEdit.text()
        self.cc = toFloat(a, "Неверное значение концентрации вещества С", WrongCcValue)

    def readListRange(self):
        a = self.numOfDotsSpinBox.text()
        self.n = toInt(a, "Неверное значение размера списка")
        if self.n < 2:
            self.n = 0
            raise WrongValueException("Неверное значение размера списка")
