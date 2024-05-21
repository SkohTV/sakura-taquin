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

    # Define some variables
    n = self.model.level.value()
    self.directions = ['up', 'down', 'left', 'right']

    # Do some random moves
    for i in range(n**2 * 50):
      dir = random.choice(self.directions)
      self.model.move_img(dir, render=False)

    # Move blank square to right max
    val = True
    while (val):
      val = self.model.move_img('right', render=False)

    # Move blank square to bottom max
    val = True
    while (val):
      val = self.model.move_img('down', render=False)

    # If the image is already correct, then re-randomize
    if self.model.full_check():
      self.randomize()
      return

    # Regenerate image
    self.model.image_center.generate_image()

