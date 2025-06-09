# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QMainWindow, QDesktopWidget, QPushButton
from PyQt5.QtCore import Qt
from UI.question import Question

class Quest_btn(QPushButton):
    def __init__(self, text, id, parent=None):
        super().__init__(text, parent)
        self.id = id
        self.par = parent # Доступ к родительскому виджету(окно с вопросами)
        self.clicked.connect(self.press_btn)

    def press_btn(self):
        #print(str(self.objectName))
        self.setText("id = {}".format(self.id))
        self.setEnabled(False)
        self.setStyleSheet("background-color: red;")

        self.par.hide()
        self.quest_window = Question(self.par) # передаю в новое окно доступ к окну с меню
        self.quest_window.show()
        
    

    