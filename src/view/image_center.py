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
      print(x, y)
      final.paste(image.im, (x, y))

    self.set_image()





  # def __init__(self, model: Game) -> None:
  #   super().__init__()
  #   self.model = model
  #   self.grid = QGridLayout()
  #   self.setLayout(self.grid)
  #   self.positions: list[tuple[int, int]] = []
  #
  #   self.blank: Square = None # type: ignore
  #   self.next_to_blank = None # type: ignore
  #
  #
  # def add_image(self, square: Square, is_blank = False) -> None:
  #   x = square.x_pos 
  #   y = square.y_pos
  #
  #   self.grid.addWidget(square, y, x)
  #   self.positions.append((x, y))
  #
  #   if is_blank:
  #     self.set_new_blank(x, y, square)
  #
  #
  # def set_new_blank(self, x: int, y: int, blank: Square) -> None:
  #   self.blank = blank
  #   self.next_to_blank = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
  #
  #
  # def change_size(self, new_size: int) -> None:
  #   self.setFixedSize(new_size, new_size)
  #
  #
  # def swap_with_blank(self, sq: Square) -> None:
  #   blank = self.blank
  #   n = self.model.level.value() - 1
  #
  #   # print(sq.x_pos + sq.y_pos*n)
  #   # self.grid.removeWidget(sq)
  #   self.grid.removeWidget(blank)
  #
  #   # Swap coords
  #   old_pos = (sq.x_pos, sq.y_pos)
  #   sq.x_pos, sq.y_pos = blank.x_pos, blank.y_pos
  #
  #   # self.add_image(sq)
  #   # self.add_image(blank, is_blank=True)
  #
  #
  # 
  # def full_render(self) -> None:
  #   '''Re-render the grid, by removing all widgets from it then adding them back (full refresh)'''
  #   # Remove old widget from grid
  #   for i, _ in self.model.image_array:
  #     self.grid.removeWidget(i)
  #
  #   n = self.model.level.value()
  #
  #   for idx, itm in enumerate(self.model.image_array):
  #     # Add new widget to grid
  #     new = itm[0]
  #     new.x_pos, new.y_pos = idx%n, idx//n
  #     self.grid.addWidget(new, *self.positions[idx]) 
  #
  #
