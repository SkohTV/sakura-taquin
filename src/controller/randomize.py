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
    '''blablabla'''
    # resets
    self.model.count.reset()
    self.model.timer.reset()
    self.model.game = True

    blank = self.model.image_array[-1]
    n = self.model.level.value()
    blank.current_x, blank.current_y = n - 1, n - 1

    first_images = self.model.image_array[:-1]
    positions = []

    for i in first_images:
      positions.append((i.true_x, i.true_y))
    random.shuffle(positions)

    for itm, (x, y) in zip(first_images, positions):
      itm.current_x, itm.current_y = x, y
      
    self.model.image_center.generate_image()

