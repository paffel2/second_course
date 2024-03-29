from PyQt5 import QtCore, QtGui, QtWidgets
from functions import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# Класс для отрисовки графика
class Canvas(FigureCanvas):
    def __init__(self, parent=None, xs=[], ys=[]):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(Canvas, self).__init__(fig)


# класс для окна приложения
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # заполнение виджета с графиком
        self.canvas = Canvas(self)
        self.canvas_layout = QtWidgets.QVBoxLayout()
        self.canvas_layout.addWidget(self.canvas)
        self.plotWidget = QtWidgets.QWidget(self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(290, 30, 501, 531))
        self.plotWidget.setStyleSheet("border: 1px solid black;")
        self.plotWidget.setObjectName("plotWidget")
        self.plotWidget.setLayout(self.canvas_layout)

        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.pix = QtGui.QPixmap("./project1/img.png")
        self.imageLabel.setGeometry(QtCore.QRect(35, 360, 225, 93))
        self.imageLabel.setPixmap(self.pix)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(12, 32, 271, 171))
        self.widget1.setObjectName("widget1")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # поле для значения верхней границы
        self.high_border_label = QtWidgets.QLabel(self.widget1)
        self.high_border_label.setObjectName("high_border_label")
        self.gridLayout.addWidget(self.high_border_label, 0, 0, 1, 1)
        self.high_border_input_line = QtWidgets.QLineEdit(self.widget1)
        self.high_border_input_line.setObjectName("high_border_input_line")
        self.gridLayout.addWidget(self.high_border_input_line, 0, 1, 1, 1)

        # поле для значения нижней границы
        self.low_border_label = QtWidgets.QLabel(self.widget1)
        self.low_border_label.setObjectName("low_border_label")
        self.gridLayout.addWidget(self.low_border_label, 1, 0, 1, 1)
        self.low_border_input_line = QtWidgets.QLineEdit(self.widget1)
        self.low_border_input_line.setEnabled(True)
        self.low_border_input_line.setObjectName("low_border_input_line")
        self.gridLayout.addWidget(self.low_border_input_line, 1, 1, 1, 1)

        self.step_label = QtWidgets.QLabel(self.widget1)
        self.step_label.setObjectName("step_label")
        self.gridLayout.addWidget(self.step_label, 2, 0, 1, 1)
        self.step_input_line = QtWidgets.QLineEdit(self.widget1)
        self.step_input_line.setEnabled(True)
        self.step_input_line.setText("0.1")
        self.step_input_line.setObjectName("step_input_line")
        self.gridLayout.addWidget(self.step_input_line, 2, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        # кнопка для запуска вычисления
        self.count_button = QtWidgets.QPushButton(self.widget1)
        self.count_button.setObjectName("count_button")
        self.gridLayout_2.addWidget(self.count_button, 0, 0, 1, 1)

        # кнопка для запуска повторного вычисления
        self.reset_button = QtWidgets.QPushButton(self.widget1)
        self.reset_button.setObjectName("reset_button")
        self.reset_button.setEnabled(False)
        self.gridLayout_2.addWidget(self.reset_button, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # связь кнопок с действиями
        self.count_button.clicked.connect(self.count_click)
        self.reset_button.clicked.connect(self.reset_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Построение графика функции")
        )
        self.high_border_label.setText(_translate("MainWindow", "Верхняя граница"))
        self.low_border_label.setText(_translate("MainWindow", "Нижняя граница"))
        self.step_label.setText(_translate("MainWindow", "Шаг вычисления"))
        self.count_button.setText(_translate("MainWindow", "Вычисление"))
        self.reset_button.setText(_translate("MainWindow", "Повторить"))

    # функция для отправки окна с ошибкой
    def send_error(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return_value = msg_box.exec()
        if return_value == QtWidgets.QMessageBox.Ok:
            self.high_border_input_line.setText("")
            self.low_border_input_line.setText("")
            self.step_input_line.setText("0.1")

    # действие для рассчета и черчения графика
    def count_click(self):
        x_n = self.high_border_input_line.text()
        x_0 = self.low_border_input_line.text()
        x_step = self.step_input_line.text()
        if not checkFloat(x_n):
            self.send_error("Неверно задана верхняя граница")
        elif not checkFloat(x_0):
            self.send_error("Неверно задана нижняя граница")
        elif not checkFloat(x_step):
            self.send_error("Неверно задан шаг вычисления")
        else:
            x_n = float(x_n)
            x_0 = float(x_0)
            x_step = float(x_step)
            self.high_border_input_line.setEnabled(False)
            self.low_border_input_line.setEnabled(False)
            self.step_input_line.setEnabled(False)
            (x, y) = countPoints(x_0, x_n, x_step)
            self.canvas.axes.plot(x, y, color="g")
            self.canvas.draw()
            self.count_button.setEnabled(False)
            self.reset_button.setEnabled(True)

    # очистка полей перед повторным рассчетом
    def reset_click(self):
        self.high_border_input_line.setText("")
        self.high_border_input_line.setEnabled(True)
        self.low_border_input_line.setText("")
        self.low_border_input_line.setEnabled(True)
        self.step_input_line.setText("0.1")
        self.step_input_line.setEnabled(True)
        self.canvas.axes.clear()
        self.canvas.draw()
        self.count_button.setEnabled(True)
        self.reset_button.setEnabled(False)
