# write the code for main app and first screen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QVBoxLayout,QPushButton

app = QApplication([])
error = QWidget()
error.setWindowTitle('My App')
error.resize(500,300)
winner = QLabel('Hello,World!')
winner_3 = QLabel('?')
winner_2 = QPushButton('Click!')
line = QVBoxLayout()
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(winner_3, alignment=Qt.AlignCenter)
line.addWidget(winner_2, alignment=Qt.AlignCenter)
error.setLayout(line)
from random import randint
def show_winner():
    number = str(randint(0,99))
    winner_3.setText(number)
    winner.setText('Winner:')
winner_2.clicked.connect(show_winner)
error.show()
app.exec_()
