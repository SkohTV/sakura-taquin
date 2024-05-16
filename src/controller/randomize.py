from PySide6.QtWidgets import QPushButton
# import random


class Randomize(QPushButton):
  '''Le boutton randomize permet de mélanger les cases de la grille du taquin game'''

  def __init__(self) -> None:
    super().__init__()
    self.model = None
    # self.clicked.connect(self.randomize) #n'appelle pas la fonction car pas de parentheses

  # def randomize(self) -> None:
  #     tmp = [i for i in range(25)]
  #     random.shuffle(tmp)
