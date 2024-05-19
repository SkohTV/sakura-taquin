# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6 import QtGui
from PySide6.QtWidgets import QLabel
from PIL.ImageQt import ImageQt


class Image_end(QLabel):
  '''Blablabla'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model

  def set_image(self) -> None:
    im = self.model.image_full
    pixmap = QtGui.QPixmap.fromImage(ImageQt(im))
    self.setPixmap(pixmap.scaled(600, 600))

