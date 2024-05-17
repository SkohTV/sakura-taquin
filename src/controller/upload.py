# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6.QtWidgets import QFileDialog, QPushButton


class Upload(QPushButton):
  '''Bouton pour upload des images'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setText('Import')
    self.clicked.connect(self.open_file_explorer)

  def open_file_explorer(self) -> None:
    self.model.image_path, _ = QFileDialog.getOpenFileName()
    self.model.load_image()
    self.model.image_end.set_image()
