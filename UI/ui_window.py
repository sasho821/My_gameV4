import imp
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtCore import Qt

class startForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,600)
        self.setObjectName("registration_form")

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.main_layout = QWidget()
        self.main_layout.setObjectName("mn_lt")

        self.setStyleSheet("""
            #mn_lt {
                background: #E3E3E3;
                border-radius: 30px;
            }
            #registration_form{
                background: transparent;
            }
        """)

        self.setCentralWidget(self.main_layout)