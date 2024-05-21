# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6.QtWidgets import QFileDialog, QPushButton



class Upload(QPushButton):
  '''Make the user pick an image in their files for the game'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setText('Import')
    self.clicked.connect(self.open_file_explorer)


  def open_file_explorer(self) -> None:
    '''Open a file explorer and allow user to select an image from it'''
    self.model.image_path, _ = QFileDialog.getOpenFileName() # Open file explorer and get file path from it
    self.model.load_image()
    self.model.cut_image()

