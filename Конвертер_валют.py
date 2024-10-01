import sys

from PyQt5.QtWidgets import (QSizePolicy, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QApplication,
                             QLineEdit, QComboBox, QMainWindow, QAction, QLabel)

CURRENCIES = {
    'Рубль': 1,
    'Доллар': 93,
    'Евро': 104,
    'Юань': 13,
    'Фунт стерлингов': 125,
    'Египетский фунт': 19,
    'Белорусский рубль': 29
}


class ConvertWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Конвертер валют 2024')

        self.main_layout = QHBoxLayout(self)
        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)

        self.input_value = QLineEdit(self)
        self.input_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_type = QComboBox(self)
        self.input_type.addItems(CURRENCIES.keys())
        self.input_type.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.convert_btn = QPushButton('-->', self)
        self.convert_btn.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_type = QComboBox(self)
        self.output_type.addItems(CURRENCIES.keys())
        self.output_type.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_layout.addWidget(self.input_value)
        self.input_layout.addWidget(self.input_type)

        self.output_layout.addWidget(self.output_value)
        self.output_layout.addWidget(self.output_type)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.convert_btn)
        self.main_layout.addLayout(self.output_layout)

        self.setLayout(self.main_layout)

    def convert(self):
        input = float(self.input_value.text()) * CURRENCIES[self.input_type.currentText()]
        output = input / CURRENCIES[self.output_type.currentText()]
        self.output_value.setText(f'{round(output, 2)}')


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Об этой программе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText('Это моя вторая программа на PyQT!!!\n Конвертер валют')
        self.layout().addWidget(self.info)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Моя новая программа')
        self.setCentralWidget(ConvertWindow())

        self.about_action = QAction(self)
        self.about_action.setText('Об этой программе')
        self.about_action.triggered.connect(self.about)
        self.menuBar().addAction(self.about_action)

        self.about_window = AboutWindow()

    def about(self):
        self.about_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = MainWindow()
    program.show()
    sys.exit(app.exec())















