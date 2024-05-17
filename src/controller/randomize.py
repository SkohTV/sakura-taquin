# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6.QtWidgets import QPushButton
# import random



class Randomize(QPushButton):
  '''Le boutton randomize permet de mélanger les cases de la grille du taquin game'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setText('Randomize')
    # self.clicked.connect(self.randomize) #n'appelle pas la fonction car pas de parentheses

  # def randomize(self) -> None:
  #     tmp = [i for i in range(25)]
  #     random.shuffle(tmp)
