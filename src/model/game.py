from PySide6 import QtGui
from PySide6.QtWidgets import QWidget


class Game(QWidget):
  '''Core of game window'''

  def __init__(self) -> None:
    super().__init__()
    self.grid = ...

    # self.setLayout(self.grid)
    self.setWindowTitle('Sakura\'s Taquin')
    self.setMinimumSize(300, 400)
    self.setFont(QtGui.QFont('Arial', 18))

