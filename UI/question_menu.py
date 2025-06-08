# Окно с вопросами
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class QuestionMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        print("QuestionMenuWindow is openned")
        # Устанавливаем центральный виджет
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Создаем GridLayout
        grid_layout = QGridLayout()

        # Создаю элементы

        centralWidget.setLayout(grid_layout)

