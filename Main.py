import PySide2
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox

import Stocks
import StockFrame


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setWindowTitle("StockHelper")

        self.setFixedSize(400, 300)

        self.button1 = QtWidgets.QPushButton("Обновить")
        self.button2 = QtWidgets.QPushButton("Запустить")
        self.button3 = QtWidgets.QPushButton("Остановить и выйти")

        self.label1 = QtWidgets.QLabel("Цена акции:")
        self.label1.setMinimumWidth(70)

        self.label2 = QtWidgets.QLabel("Время обновления(сек):")
        self.label2.setMinimumWidth(70)

        self.label_5min = QtWidgets.QLabel("5 минут")
        self.label_5min.setMinimumWidth(70)
        self.label1_15min = QtWidgets.QLabel("15 минут")
        self.label1_15min.setMinimumWidth(70)
        self.label1_1hour = QtWidgets.QLabel("1 час")
        self.label1_1hour.setMinimumWidth(70)
        self.label1_1day = QtWidgets.QLabel("1 день")
        self.label1_1day.setMinimumWidth(70)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItem("Sberbank")
        self.comboBox.addItem("Gazprom")

        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit4 = QtWidgets.QLineEdit(self)
        self.lineEdit5 = QtWidgets.QLineEdit(self)
        self.lineEdit5.setEnabled(False)
        self.lineEdit6 = QtWidgets.QLineEdit(self)
        self.lineEdit6.setText("60")

        layout_v = QtWidgets.QVBoxLayout()
        layout_h1 = QtWidgets.QHBoxLayout()
        layout_h2 = QtWidgets.QHBoxLayout()
        layout_h3 = QtWidgets.QHBoxLayout()
        layout_h4 = QtWidgets.QHBoxLayout()
        layout_h5 = QtWidgets.QHBoxLayout()
        layout_h6 = QtWidgets.QHBoxLayout()
        layout_h7 = QtWidgets.QHBoxLayout()
        layout_h8 = QtWidgets.QHBoxLayout()
        layout_h9 = QtWidgets.QHBoxLayout()
        layout_h10 = QtWidgets.QHBoxLayout()

        # Выбор акций
        layout_h1.addWidget(self.comboBox)
        # Цена акций
        layout_h2.addWidget(self.label1)
        layout_h2.addWidget(self.lineEdit5)

        # Кнопки
        layout_h3.addWidget(self.button1)
        layout_h4.addWidget(self.button2)
        layout_h4.addWidget(self.label2)
        layout_h4.addWidget(self.lineEdit6)
        layout_h6.addWidget(self.button3)

        # Рекомендация
        layout_h7.addWidget(self.label_5min)
        layout_h7.addWidget(self.lineEdit1)

        layout_h8.addWidget(self.label1_15min)
        layout_h8.addWidget(self.lineEdit2)

        layout_h9.addWidget(self.label1_1hour)
        layout_h9.addWidget(self.lineEdit3)

        layout_h10.addWidget(self.label1_1day)
        layout_h10.addWidget(self.lineEdit4)

        layout_v.addLayout(layout_h1)
        layout_v.addLayout(layout_h2)
        layout_v.addLayout(layout_h3)
        layout_v.addLayout(layout_h4)
        layout_v.addLayout(layout_h5)
        layout_v.addLayout(layout_h6)
        layout_v.addLayout(layout_h7)
        layout_v.addLayout(layout_h8)
        layout_v.addLayout(layout_h9)
        layout_v.addLayout(layout_h10)
        layout_v.addItem(QtWidgets.QSpacerItem(1, 1,
                                               QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Expanding))

        self.setLayout(layout_v)

        self.button1.clicked.connect(self.click_button)
        self.button2.clicked.connect(self.start)
        self.button3.clicked.connect(self.stop)

    def click_button(self):
        name_stock = self.comboBox.currentText()

        res5min = self.lineEdit1.text()
        res15min = self.lineEdit2.text()
        res1hour = self.lineEdit3.text()
        res1day = self.lineEdit4.text()
        message = ""

        self.button1.clicked.connect(Stocks.start_prog(name_stock))
        self.lineEdit5.setText(str(StockFrame.get_price(name_stock)))

        for_text = StockFrame.get_technikal_5min(name_stock)
        if for_text == "Активно покупать":
            self.lineEdit1.setText(for_text)
            self.lineEdit1.setStyleSheet('background-color: green')
        elif for_text == "Покупать":
            self.lineEdit1.setText(for_text)
            self.lineEdit1.setStyleSheet('background-color: green')
        elif for_text == "Активно продавать":
            self.lineEdit1.setText(for_text)
            self.lineEdit1.setStyleSheet("background-color: red")
        elif for_text == "Продавать":
            self.lineEdit1.setText(for_text)
            self.lineEdit1.setStyleSheet("background-color: red")
        else:
            self.lineEdit1.setText(for_text)
            self.lineEdit1.setStyleSheet("background-color: white")

        if res5min != self.lineEdit1.text():
            message += "Произошли изменения в 5 минутах. c " + res5min + " на " + self.lineEdit1.text() + "\n"

        for_text = StockFrame.get_technikal_15min(name_stock)
        if for_text == "Активно покупать":
            self.lineEdit2.setText(for_text)
            self.lineEdit2.setStyleSheet('background-color: green')
        elif for_text == "Покупать":
            self.lineEdit2.setText(for_text)
            self.lineEdit2.setStyleSheet('background-color: green')
        elif for_text == "Активно продавать":
            self.lineEdit2.setText(for_text)
            self.lineEdit2.setStyleSheet("background-color: red")
        elif for_text == "Продавать":
            self.lineEdit2.setText(for_text)
            self.lineEdit2.setStyleSheet("background-color: red")
        else:
            self.lineEdit2.setText(for_text)
            self.lineEdit2.setStyleSheet("background-color: white")

        if res15min != self.lineEdit2.text():
            message += "Произошли изменения в 15 минутах. c " + res15min + " на " + self.lineEdit2.text() + "\n"

        for_text = StockFrame.get_technikal_1hour(name_stock)
        if for_text == "Активно покупать":
            self.lineEdit3.setText(for_text)
            self.lineEdit3.setStyleSheet('background-color: green')
        elif for_text == "Покупать":
            self.lineEdit3.setText(for_text)
            self.lineEdit3.setStyleSheet('background-color: green')
        elif for_text == "Активно продавать":
            self.lineEdit3.setText(for_text)
            self.lineEdit3.setStyleSheet("background-color: red")
        elif for_text == "Продавать":
            self.lineEdit3.setText(for_text)
            self.lineEdit3.setStyleSheet("background-color: red")
        else:
            self.lineEdit3.setText(for_text)
            self.lineEdit3.setStyleSheet("background-color: white")

        if res1hour != self.lineEdit3.text():
            message += "Произошли изменения в 1 часе c " + res1hour + " на " + self.lineEdit3.text() + "\n"

        for_text = StockFrame.get_technikal_1day(name_stock)
        if for_text == "Активно покупать":
            self.lineEdit4.setText(for_text)
            self.lineEdit4.setStyleSheet('background-color: green')
        elif for_text == "Покупать":
            self.lineEdit4.setText(for_text)
            self.lineEdit4.setStyleSheet('background-color: green')
        elif for_text == "Активно продавать":
            self.lineEdit4.setText(for_text)
            self.lineEdit4.setStyleSheet("background-color: red")
        elif for_text == "Продавать":
            self.lineEdit4.setText(for_text)
            self.lineEdit4.setStyleSheet("background-color: red")
        else:
            self.lineEdit4.setText(for_text)
            self.lineEdit4.setStyleSheet("background-color: white")

        if res1day != self.lineEdit4.text():
            message += "Произошли изменения в 1 дне: " + res1day + " на " + self.lineEdit4.text() + "\n"

        if message != "":
            self.podskazka(message)

    def on_check(self, text):
        try:
            return text
        except ValueError:
            QMessageBox.warning(self, 'Внимание',
                                'Введено невалидное число в "Время обновление". Измените его: "{}"'.format(text))

    def start(self):
        time_sleep = self.lineEdit6.text()
        self.on_check(time_sleep)
        time_sleep = int(time_sleep)
        timer = PySide2.QTimer(self)
        timer.singleShot(time_sleep, self.click_button)

    def stop(self):
        app.quit()

    def podskazka(self, text):
        QMessageBox.information(self, 'Внимание',
                                'На рынке изменилась ситуация \n "{}"'.format(text))


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    myapp = MainWindow()
    myapp.show()
    # myapp.click_button()
    app.exec_()
