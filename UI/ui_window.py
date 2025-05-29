from PyQt5.QtWidgets import (QWidget, QMainWindow, QDesktopWidget,
QLineEdit, QGridLayout, QVBoxLayout)
from PyQt5.QtCore import Qt

class startForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(900,600) # Устанавливаю размеры окна
        self.setObjectName("registration_form") # Задаю имя окна
        self.center() # Выравнивание по центру

        self.setWindowFlags(Qt.FramelessWindowHint) # Безрамочный режим
        self.setAttribute(Qt.WA_TranslucentBackground, True) # Прозрачный фон

        self.main_layout = QWidget()
        self.main_layout.setObjectName("mn_lt")
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
        self.main_layout.addLayout(self.grid)
        self.setCentralWidget(self.main_layout)

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
        self.vbox = QVBoxLayout()
        
        for i in range(5):
            team_inp = QLineEdit()
            team_inp.setObjectName("team_inp_field_{}".format(i))
            self.vbox.addWidget(team_inp)
            
        self.grid.addLayout(self.vbox, 0, 1)