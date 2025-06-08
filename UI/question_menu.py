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

        # Создаем GridLayout - общий
        grid_layout = QGridLayout()
        # Создаем GridLayout - для вопросов
        quest_grid_layout = QGridLayout()

        # Создаю элементы
        self.theme_name_lbl = QLabel("Название темы")

        # Размещаю элементы в сетке вопросов
        # 1. Размещаю название категорий
        for i in range(5):
            buf_lbl = QLabel("Категория_{}".format(i))
            buf_lbl.setObjectName("cat_name_{}".format(i))
            quest_grid_layout.addWidget(buf_lbl, (i + 1), 1, alignment=Qt.AlignCenter)

        # Размещаю элементы в общей сетке
        grid_layout.addWidget(self.theme_name_lbl, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addLayout(quest_grid_layout, 2, 1, alignment=Qt.AlignCenter)

        # Настройка общей сетки
        # Настройка растяжения строчек
        grid_layout.setRowStretch(1, 1) 
        grid_layout.setRowStretch(2, 5)

        centralWidget.setLayout(grid_layout)

