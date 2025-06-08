# Окно входа в игру

from PyQt5.QtWidgets import (QWidget, QMainWindow, QDesktopWidget,
QLineEdit, QGridLayout, QVBoxLayout, QCheckBox, QPushButton)
from PyQt5.QtCore import Qt

from UI.question_menu import QuestionMenuWindow

class startForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(900,600) # Устанавливаю размеры окна
        self.setObjectName("registration_form") # Задаю имя окна
        self.center() # Выравнивание по центру

        self.setWindowFlags(Qt.FramelessWindowHint) # Безрамочный режим
        self.setAttribute(Qt.WA_TranslucentBackground, True) # Прозрачный фон
        
        # Виджет с главной разметкой, в него размещается главный layout
        self.main_layout = QWidget()
        self.main_layout.setObjectName("mn_lt")
        # Разметка-сетка, размещается в main_layout, на неё вешается все остальное
        self.grid = QGridLayout()

        # Стили
        self.setStyleSheet("""
            #mn_lt {
                background: #E3E3E3;
            }
            #registration_form{
                background: transparent;
            }
        """)

        # метод для размещения всех элементов на форме
        self.add_team_inp_field()

        self.main_layout.setLayout(self.grid)
        self.setCentralWidget(self.main_layout)
        # События
        self.exit_btn.clicked.connect(self.close) # Срабатывает при нажатии на кнопку "Выход"
        self.start_btn.clicked.connect(self.start_game) # Срабатывает при нажатии на кнопку "Старт"

    # Метод для выравнивания главного окна по центру
    def center(self):
        # Получаем геометрию доступной части экрана
        desktop = QDesktopWidget()
        screenRect = desktop.availableGeometry()

        # Получаем геометрию текущего окна
        windowRect = self.frameGeometry()

        # Рассчитываем центральную точку экрана
        centerPoint = screenRect.center()

        # Рассчитываем новые координаты окна, чтобы оно было в центре
        windowRect.moveCenter(centerPoint)

        # Перемещаем окно в рассчитанную позицию
        self.move(windowRect.topLeft())


    # Добавление в основную разметку полей ввода
    def add_team_inp_field(self):
        # Вертикальная стопка с полями для команд и кнопками
        self.vbox = QVBoxLayout()
        # Вертикальная стопка с чекбоксами
        self.setingsvbox = QVBoxLayout()
        
        # Добавляю поля с названиями команд
        for i in range(5):
            team_inp = QLineEdit()
            team_inp.setObjectName("team_inp_field_{}".format(i))
            self.vbox.addWidget(team_inp, alignment=Qt.AlignTop)
        
        # Кнопка "старт"
        self.start_btn = QPushButton("Начать")
        # Кнопка "Выход"
        self.exit_btn = QPushButton("Выход")

        # Добавляю настройки
        self.random_queue_box = QCheckBox("Случайная очередность")
        self.cat_in_bag_box = QCheckBox("Кот в мешке")
        self.mines_box = QCheckBox("Мины")
        self.change_game_btn = QPushButton("Выбрать тему")
        # Размещаю настройки на форме
        self.setingsvbox.addWidget(self.change_game_btn, alignment=Qt.AlignTop)
        self.setingsvbox.addWidget(self.random_queue_box, alignment=Qt.AlignTop)
        self.setingsvbox.addWidget(self.cat_in_bag_box, alignment=Qt.AlignTop)
        self.setingsvbox.addWidget(self.mines_box, alignment=Qt.AlignTop)
        # Размещаю кнопки на форме
        self.vbox.addWidget(self.start_btn)
        self.vbox.addWidget(self.exit_btn)
        # Размещая вертикальные стопки на главной разметке
        self.grid.addLayout(self.vbox, 0, 2, alignment=Qt.AlignTop)
        self.grid.addLayout(self.setingsvbox, 0, 1, alignment=Qt.AlignTop)
        # Устанавливаю параметры пропорций столбцов
        self.grid.setColumnStretch(1, 2)
        self.grid.setColumnStretch(2, 1)

    
    def start_game(self):
        print("Start Game")
        self.close()
        self.questionMenuWindow = QuestionMenuWindow()
        self.questionMenuWindow.show()
        