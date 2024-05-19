# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PIL.ImageQt import ImageQt
from PIL.Image import Image



class Square(QPushButton):
  '''Un morceau de l\'image, peut etre deplacee'''

  def __init__(self, model: Game, image: Image, dim: int) -> None:
    super().__init__()
    self.model = model

    self.label = QLabel()
    self.wrap = QVBoxLayout()
    self.wrap.addWidget(self.label)
    self.wrap.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.wrap)

    image_qt = ImageQt(image)
    pixmap = QPixmap(image_qt)
    self.label.setPixmap(pixmap.scaled(dim, dim))
    self.setFixedSize(dim, dim)

