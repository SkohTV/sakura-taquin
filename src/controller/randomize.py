# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6.QtWidgets import QPushButton
import random



class Randomize(QPushButton):
  '''Le boutton randomize permet de mélanger les cases de la grille du taquin game'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setText('Randomize')
    self.clicked.connect(self.randomize) #n'appelle pas la fonction car pas de parentheses

  def randomize(self) -> None:
    self.model.image_array.sort(key=lambda x: 99999999 if x[1] is None else x[1])
    squares = self.model.image_array[:-1]
    random.shuffle(squares)
    self.model.image_array[:-1] = squares
    self.model.grid.full_render()

