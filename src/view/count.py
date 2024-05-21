# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6 import QtCore
from PySide6.QtWidgets import QLabel


class Count(QLabel):
  '''Counter of the number of moves played since first move'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.count = 0
    self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


  def add(self) -> None:
    '''Add one to the counter'''
    self.count += 1
    self.setText(f'{self.count} coups')


  def reset(self) -> None:
    '''Set the counter back to 0'''
    self.count = 0
    self.setText('- coups')

