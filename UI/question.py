# Окно с вопросом

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from modules.db import get_data
import random
from modules.config import Config
#from UI.controls import QuestionData

# Класс QuestionData предназначен для хранения в себе всех данных о вопросе. Он должен формироваться при нажатии кнопки
# вопроса и передаваться в окно с вопросом.
class QuestionData():
    def __init__(self, id):
        # получаем все вопросы по данной кнопке
        data = get_data(Config.DATABASE_PATH, "SELECT * FROM questions WHERE id = '{}'".format(str(id)))
        n_quest = len(data) # Количество вопросов по теме
        rand = random.randint(0, n_quest-1) # Случайное число из диапозона вопрос
        selected_quest = data[rand] # Выбираем вопрос из общего числа вопросов

        self.selected_quest = selected_quest


class Question(QMainWindow):
    def __init__(self, id, q_cost, parent:QMainWindow=None):
        super().__init__()
        self.showFullScreen()
        self.parent_window = parent # Получаю доступ к родительскому окну
        self.q_cost = q_cost # Получаю стоимость вопроса в баллах
        central_widget = QWidget() # Cоздаю главный виджет для разметки

        self.grid_layout = QGridLayout() # Cоздаю разметку
        
        self.time_bar = QProgressBar()
        self.time_bar.setFixedSize(600,100)
        # Создаю фрейм и задаю его параметры, в нем будет размещаться вопросы
        self.question_frame = QFrame()
        self.question_frame.setFrameShape(QFrame.Box)
        self.question_frame.setFrameShadow(QFrame.Raised)
        self.question_frame.setFixedSize(1400,500)
        
        # Размещаю элементы на сетке
        self.grid_layout.addWidget(self.time_bar, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        self.grid_layout.addWidget(self.question_frame, 2, 1, 1, 2, alignment=Qt.AlignCenter)
        
        # Задаю пропорции сетки
        self.grid_layout.setRowStretch(1, 1)
        self.grid_layout.setRowStretch(2, 2)
        self.grid_layout.setRowStretch(3, 1)
        self.grid_layout.setRowStretch(4, 1)

        central_widget.setLayout(self.grid_layout)

        self.setCentralWidget(central_widget)

        question = QuestionData(id)

        self.set_question(question)
        

    # Метод который задает вопрос на форму
    def set_question(self, quest:QuestionData):
        if quest == None:
            return

        print(quest.selected_quest)
        quest_type = quest.selected_quest[10]
        if quest_type == 0: # Тип вопроса - 0
            # Создаю кнопки
            ans_btn_1 = AnwserBtn("Ответ 1",self.parent_window, self)
            ans_btn_2 = AnwserBtn("Ответ 2",self.parent_window, self)
            ans_btn_3 = AnwserBtn("Ответ 3",self.parent_window, self)
            ans_btn_4 = AnwserBtn("Ответ 4",self.parent_window, self)

            self.grid_layout.addWidget(ans_btn_1, 3, 1, alignment=Qt.AlignCenter)
            self.grid_layout.addWidget(ans_btn_2, 4, 1, alignment=Qt.AlignCenter)
            self.grid_layout.addWidget(ans_btn_3, 3, 2, alignment=Qt.AlignCenter)
            self.grid_layout.addWidget(ans_btn_4, 4, 2, alignment=Qt.AlignCenter)

            ans_btn_1.setText(quest.selected_quest[3])
            ans_btn_2.setText(quest.selected_quest[4])
            ans_btn_3.setText(quest.selected_quest[5])
            ans_btn_4.setText(quest.selected_quest[6])

            ans_btns = [ans_btn_1, ans_btn_2, ans_btn_3, ans_btn_4]
            
            ans_btns[quest.selected_quest[7]].right = True

            question_lbl = QLabel(quest.selected_quest[2])

            frame_layout = QVBoxLayout()
            frame_layout.addWidget(question_lbl, alignment=Qt.AlignCenter)

            self.question_frame.setLayout(frame_layout)
            self.question_frame.show()
        # Для начала нужно понять тип вопроса    


class AnwserBtn(QPushButton):
    def __init__(self, text, parent:QMainWindow=None, form:QMainWindow=None):
        super().__init__()
        self.setText(text)
        self.par = parent # Получаю доступ к окну с вопросами
        self.form = form

        self.setFixedSize(600,200)

        self.right = False

        self.clicked.connect(self.on_click)
    

    def on_click(self):
        if self.right:
            QMessageBox.information(self, "Верный ответ", "Вы ответили правильно!\n + {} баллов".format(self.form.q_cost))
        else:
            QMessageBox.critical(self,"Неверный ответ", "Вы ошиблись, повезет в другой раз \n - {} баллов".format(self.form.q_cost))

        self.form.close()
        self.par.show()
        print("close window")


