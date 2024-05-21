# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PIL import Image 
from PIL.ImageQt import ImageQt
from PySide6 import QtGui
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLabel


class Image_center(QLabel):
  '''Blablabla'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model


  def set_image(self) -> None:
    '''blabla'''
    im = self.model.image_shuffled
    pixmap = QtGui.QPixmap.fromImage(ImageQt(im))
    self.setPixmap(pixmap.scaled(600, 600))


  def generate_image(self) -> None:
    '''blabla'''
    self.model.image_shuffled = Image.new('RGB', (self.model.full_size, self.model.full_size), '#000000')
    final = self.model.image_shuffled
    small_size = self.model.small_size

    for image in self.model.image_array:
      x = image.current_x * small_size
      y = image.current_y * small_size
      final.paste(image.im, (x, y))

    self.set_image()

  def final_image(self) -> None:
    self.model.image_shuffled = self.model.image_full
    self.set_image()

