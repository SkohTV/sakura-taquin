# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6 import QtCore
from PySide6.QtWidgets import QLabel



class Title(QLabel):
  '''Title of the image shown'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    self.setStyleSheet('font-size: 36px')


  def change_title(self, title: str) -> None:
    '''Change the title to match the image name'''
    self.setText(title)
