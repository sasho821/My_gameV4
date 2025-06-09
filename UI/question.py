# Окно с вопросом

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Question(QMainWindow):
    def __init__(self, parent:QMainWindow=None):
        super().__init__()
        self.showFullScreen()
        self.parent_window = parent # Получаю доступ к родительскому окну

        central_widget = QWidget()

        grid_layout = QGridLayout()
        
        self.time_bar = QProgressBar()
        
        self.question_frame = QFrame()
        self.question_frame.setFrameShape(QFrame.Box)
        self.question_frame.setFrameShadow(QFrame.Raised)

        self.ans_btn_1 = AnserBtn("Ответ 1",self.parent_window, self)
        self.ans_btn_2 = AnserBtn("Ответ 2",self.parent_window, self)
        self.ans_btn_3 = AnserBtn("Ответ 3",self.parent_window, self)
        self.ans_btn_4 = AnserBtn("Ответ 4",self.parent_window, self)

        grid_layout.addWidget(self.time_bar, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.question_frame, 2, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.ans_btn_1, 3, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.ans_btn_2, 4, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.ans_btn_3, 3, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.ans_btn_4, 4, 2, alignment=Qt.AlignCenter)

        central_widget.setLayout(grid_layout)

        self.setCentralWidget(central_widget)


class AnserBtn(QPushButton):
    def __init__(self, text, parent:QMainWindow=None, form:QMainWindow=None):
        super().__init__()
        self.setText(text)
        self.par = parent # Получаю доступ к окну с вопросами
        self.form = form

        self.resize(200, 100)

        self.clicked.connect(self.on_click)
    

    def on_click(self):
        self.form.close()
        self.par.show()
        print("close window")
        