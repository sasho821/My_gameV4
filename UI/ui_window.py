# Окно входа в игру

from PyQt5.QtWidgets import (QWidget, QMainWindow, QDesktopWidget,
QLineEdit, QGridLayout, QVBoxLayout, QCheckBox, QPushButton, QFileDialog,
QLabel)
from PyQt5.QtCore import Qt

from UI.question_menu import QuestionMenuWindow

from modules.db import get_data
from modules.config import Config

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
        # Размещаю сетку с элементами на форме
        self.main_layout.setLayout(self.grid)
        self.setCentralWidget(self.main_layout)
        # События
        self.exit_btn.clicked.connect(self.close) # Срабатывает при нажатии на кнопку "Выход"
        self.start_btn.clicked.connect(self.start_game) # Срабатывает при нажатии на кнопку "Старт"
        self.change_game_btn.clicked.connect(self.select_game) # Срабатывает при нажатии на кнопку "Выбрать тему"

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
        # Вериткалььная стопка с рейтингом
        self.scoreboardvbox = QVBoxLayout()
        
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
        # Добавляю рейтинг команд по теме
        self.scoreboardvbox.addWidget(QLabel("Рейтинг команд"), alignment=Qt.AlignCenter)
        self.score_board_lbls = []
        for i in range(5):
            buf_lbl = QLabel("Команда_{}".format(i))
            buf_lbl.setObjectName("scoreboard_lbl_{}".format(i))
            self.score_board_lbls.append(buf_lbl)
            self.scoreboardvbox.addWidget(buf_lbl, alignment=Qt.AlignTop | Qt.AlignLeft)
        # Размещаю кнопки на форме
        self.vbox.addWidget(self.start_btn)
        self.vbox.addWidget(self.exit_btn)
        # Размещая вертикальные стопки на главной разметке
        self.grid.addLayout(self.vbox, 0, 2, alignment=Qt.AlignTop)
        self.grid.addLayout(self.setingsvbox, 0, 1, alignment=Qt.AlignTop)
        self.grid.addLayout(self.scoreboardvbox, 1, 1, alignment=Qt.AlignCenter)
        # Устанавливаю параметры пропорций столбцов
        self.grid.setColumnStretch(1, 2)
        self.grid.setColumnStretch(2, 1)

    
    # Метод который получает имена команд
    def get_comand_name(self):
        result = []
        for i in range(5):
            buf = self.findChild(QLineEdit, "team_inp_field_{}".format(i)).text()
            result.append(buf)
        return result

    
    def get_game_settings(self):
        pass


    def start_game(self):
        print("Start Game")
        self.close()

        # Получаю настройки и название команд для передачи в игру
        team_names = self.get_comand_name()
        print(team_names)

        self.questionMenuWindow = QuestionMenuWindow(team_names)
        self.questionMenuWindow.show()
        
    # Метод для получения пути к базе данных с вопросами
    def select_game(self):
        # Получаю путь до базы данных (банка вопросов)
        file_path = QFileDialog.getOpenFileName(None, "Выберите тему игры","","Все файлики (*)")
        # Извлекаю "прямой путь"
        database_path = str(file_path[0])
        # Сохраняю "прямой путь" к базе данных в глобальную область видимости 
        Config.DATABASE_PATH = database_path
        # Выполняю запрос на получение списка команд с сортировкой по убыванию
        team_scores = get_data(database_path, 'SELECT * FROM scores ORDER BY score DESC')
        # Расставляю название команд в таблице рейтинга
        for i in range(5):
            self.score_board_lbls[i].setText("{} - {}".format(team_scores[i][1], team_scores[i][2]))