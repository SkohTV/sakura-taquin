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
    images = self.model.image_array

    for idx, itm in enumerate(images):
      if itm.is_blank:
        blank = idx

    images[-1], images[blank] = images[blank], images[-1] # type: ignore

    first_images = self.model.image_array[:-1]
    positions = []

    for i in first_images:
      positions.append((i.true_x, i.true_y))
    random.shuffle(positions)

    for itm, (x, y) in zip(first_images, positions):
      itm.current_x, itm.current_y = x, y
      
    self.model.image_array[:-1] = first_images
    self.model.image_center.generate_image()

