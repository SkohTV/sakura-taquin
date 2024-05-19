# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6.QtWidgets import QGridLayout, QLabel
from controller.square import Square


class Grid(QLabel):
  '''Blablabla'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.grid = QGridLayout()
    self.setLayout(self.grid)
    self.setFixedSize(600, 600)
    self.positions: list[tuple[int, int]] = []


  def add_image(self, square: Square, x: int, y: int) -> None:
    self.grid.addWidget(square, y, x)
    self.positions.append((x, y))

  
  def full_render(self) -> None:
    '''Re-render the grid, by removing all widgets from it then adding them back (full refresh)'''
    # Remove old widget from grid
    for i in range(len(self.model.image_array)):
      self.grid.takeAt(i)

    for idx, itm in enumerate(self.model.image_array):
      # Add new widget to grid
      new = itm[0]
      self.grid.addWidget(new, *self.positions[idx]) 


