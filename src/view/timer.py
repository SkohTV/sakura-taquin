# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6 import QtCore
from PySide6.QtWidgets import QLabel


class Timer(QLabel):
  '''Affiche la duree entre le premier et le dernier coups'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setText('0.0')
    self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

  # def change_title(self, title1: str) -> None:
  #   self.setText(title1)
