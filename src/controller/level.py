# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6 import QtCore
from PySide6.QtWidgets import QSpinBox



class Level(QSpinBox):
  '''Select the dimensions in which to cut the image'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setMinimum(2)
    self.setMaximum(99)
    self.setValue(3)

    # Disable the ability to focus it (keep arrows for movement, not number up/down)
    self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus) 

    self.valueChanged.connect(self.model.cut_image)

