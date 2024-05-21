# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PIL import Image 
from PIL.ImageQt import ImageQt
from PySide6 import QtGui
from PySide6.QtWidgets import QLabel



class Image_center(QLabel):
  '''600x600 image in the center used for the game'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model


  def set_image(self) -> None:
    '''Display the stored image'''
    im = self.model.image_shuffled
    pixmap = QtGui.QPixmap.fromImage(ImageQt(im))
    self.setPixmap(pixmap.scaled(600, 600))


  def generate_image(self) -> None:
    '''Generate and store an image, from small images array'''
    
    # Create a new image to paste small image on it
    self.model.image_shuffled = Image.new('RGBA', (self.model.full_size, self.model.full_size), '#00000000')
    final = self.model.image_shuffled
    small_size = self.model.small_size

    # Paste all small images on stored image
    for image in self.model.image_array:
      x = image.current_x * small_size
      y = image.current_y * small_size
      final.paste(image.im, (x, y))

    self.set_image() # Render the image


  def final_image(self) -> None:
    '''Generate and store an image, from big full image'''
    self.model.image_shuffled = self.model.image_full # The stored image is the full image
    self.set_image() # Render the image

