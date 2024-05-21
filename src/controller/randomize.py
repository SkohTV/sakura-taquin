# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6.QtWidgets import QPushButton
import random



class Randomize(QPushButton):
  '''Shuffle the squares when clicked'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setText('Randomize')
    self.clicked.connect(self.randomize)


  def randomize(self) -> None:
    '''Shuffle the CURRENT COORDINATES of the squares and reset the position of blank square'''
    # Resets
    self.model.count.reset()
    self.model.timer.reset()
    self.model.game = True

    # Pick blank square and its coords
    blank = self.model.image_array[-1]
    n = self.model.level.value()
    blank.current_x, blank.current_y = n - 1, n - 1

    # Select all squares EXCEPT blank (last)
    first_images = self.model.image_array[:-1]
    positions = []

    # Add correct positions of all squares to list
    for i in first_images:
      positions.append((i.true_x, i.true_y))
    random.shuffle(positions) # Shuffle the list of positions

    # Set the current position of squares to shuffled position from created list
    for itm, (x, y) in zip(first_images, positions):
      itm.current_x, itm.current_y = x, y
      
    # Regenerate image
    self.model.image_center.generate_image()

