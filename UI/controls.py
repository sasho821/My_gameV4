# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QMainWindow, QDesktopWidget, QPushButton
from PyQt5.QtCore import Qt
from UI.question import Question
from modules.db import get_data
from modules.config import Config
import random

class Quest_btn(QPushButton):
    def __init__(self, text, id, parent=None):
        super().__init__(text, parent)
        self.id = id
        self.par = parent # Доступ к родительскому виджету(окно с вопросами)
        self.clicked.connect(self.press_btn)


    # Действие при нажатии кнопки с вопросом
    def press_btn(self):
        self.setText("id = {}".format(self.id)) # Меняю текст на кнопке на id кнопки (нужно для работы, на релизе уберу)
        # Делаю её неактивной и меняю цвет фона
        self.setEnabled(False)
        self.setStyleSheet("background-color: red;")

        question_data = QuestionData(self.id)

        self.par.hide() # Скрываю окно с сеткой вопросов
        self.quest_window = Question(question_data, self.par) # передаю в новое окно доступ к окну с меню
        self.quest_window.show() # Вывожу на экран окно с вопросом
        

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

        print(selected_quest)
        
