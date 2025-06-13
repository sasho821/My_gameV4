# Окно с вопросами
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from UI.controls import Quest_btn

from modules.config import Config

class QuestionMenuWindow(QMainWindow):
    def __init__(self, team_names):
        super().__init__()
        self.showFullScreen()
        self.team_names = team_names
        print("QuestionMenuWindow is openned")
        # Устанавливаем центральный виджет
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Создаем GridLayout - общий
        grid_layout = QGridLayout()
        # Создаем GridLayout - для вопросов (кнопки)
        quest_grid_layout = QGridLayout()

        # Создаю элементы
        self.theme_name_lbl = QLabel("Название темы")
        self.exit_btn = QPushButton("Выход")

        # Размещаю элементы в сетке вопросов
        # 1. Создаю и размещаю название категорий
        for i in range(5):
            buf_lbl = QLabel("Категория_{}".format(i))
            buf_lbl.setObjectName("cat_name_{}".format(i))
            quest_grid_layout.addWidget(buf_lbl, i, 1, alignment=Qt.AlignCenter)
        # 2. Создаю и размещаю кнопки
        for i in range(5): # строка
            for j in range(5): # колонна
                self.buf_btn = Quest_btn("{}".format(str((j+1)*10)), "{}{}".format(i,j), self) # создаю кнопку
                self.buf_btn.setObjectName("quest_btn_{}{}".format(i,j)) # Задаю имя объекта
                quest_grid_layout.addWidget(self.buf_btn, i, j+2, alignment=Qt.AlignCenter)

        # Создаю и размещаю и команды в статистике
        statistics_layout = QVBoxLayout() # Создаю вертикальную стопку
        #self.teams = [] # Создаю список под объекты типа Team
        self.scr_lbls_lst = [] # Создаю список текстов полей под статистику
        statistics_layout.addWidget(QLabel("Рейтинг"), alignment=Qt.AlignCenter)

        for team in team_names:
            # Создаю и добавляю объект команды в список
            team_buf = Team(team)
            #self.teams.append(team_buf)
            # Добавляю в глобальную область
            Config.teams.append(team_buf)
            # Буферные переменные для удобной вставки имени и счета в строку рейтинга
            name = Config.teams[-1].name
            score = Config.teams[-1].score
            scr_lbl = QLabel("{} \t - {}".format(name, score))
            # Добавляю текстовые метки в список для дальнейшей работы с ней
            self.scr_lbls_lst.append(scr_lbl)
            statistics_layout.addWidget(scr_lbl, alignment=Qt.AlignLeft)

        # Подсвечиваю текущую команду
        self.scr_lbls_lst[Config.cur_team].setStyleSheet("color: red;")


        # Размещаю элементы в общей сетке
        grid_layout.addWidget(self.theme_name_lbl, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addLayout(quest_grid_layout, 2, 1, alignment=Qt.AlignCenter)
        grid_layout.addLayout(statistics_layout, 2, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.exit_btn, 3, 1, 1, 2, alignment=Qt.AlignRight)

        # Настройка общей сетки
        # Настройка растяжения строчек
        grid_layout.setRowStretch(1, 1) 
        grid_layout.setRowStretch(2, 5)

        centralWidget.setLayout(grid_layout)

        # Сигналы
        self.exit_btn.clicked.connect(self.close)


    def refresh_stat(self):
        # Меняю цвет текста всех элементов к базовому
        n = len(self.scr_lbls_lst)
        for i in range(n):
            cur_team = Config.teams[i]
            self.scr_lbls_lst[i].setStyleSheet("color: black;")
            self.scr_lbls_lst[i].setText("{} \t - {}".format(cur_team.name, cur_team.score))
        # Обновляю значения 
        self.scr_lbls_lst[Config.cur_team].setStyleSheet("color: red;")


class Team():
    def __init__(self, name):
        self.name = name
        self.score = 0

