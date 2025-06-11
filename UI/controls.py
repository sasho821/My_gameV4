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
        self.q_cost = int(text) # Получаю стоимость вопроса
        self.id = id
        self.par = parent # Доступ к родительскому виджету(окно с вопросами)
        self.clicked.connect(self.press_btn)


    # Действие при нажатии кнопки с вопросом
    def press_btn(self):
        self.setText("id = {}".format(self.id)) # Меняю текст на кнопке на id кнопки (нужно для работы, на релизе уберу)
        # Делаю её неактивной и меняю цвет фона
        self.setEnabled(False)
        self.setStyleSheet("background-color: red;")

        self.par.hide() # Скрываю окно с сеткой вопросов
        # передаю в новое окно доступ к окну с меню и передаю id вопроса
        self.quest_window = Question(self.id, self.q_cost, self.par) 

        self.quest_window.show() # Вывожу на экран окно с вопросом
        


        
