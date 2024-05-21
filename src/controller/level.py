# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6 import QtCore
from PySide6.QtWidgets import QSpinBox


class Level(QSpinBox):
  ''' Une case qui permet de choisir les dimensions  de la grille '''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setMinimum(2)
    self.setMaximum(99)
    self.setValue(3)
    self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

    self.valueChanged.connect(self.model.cut_image)

