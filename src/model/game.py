from os import path
from dataclasses import dataclass

from PySide6 import QtGui
from PySide6.QtWidgets import QGridLayout, QWidget
from PIL import Image

from controller.level import Level
from controller.randomize import Randomize
from controller.upload import Upload
from view.count import Count
from view.image_center import Image_center
from view.leaderboard import Leaderboard
from view.name import Name
from controller.source import Source
from view.timer import Timer
from view.title import Title



@dataclass
class Square:
  im: Image.Image
  true_x: int
  true_y: int
  current_x: int
  current_y: int
  is_blank: bool = False


class Game(QWidget):
  '''Core of game window'''

  def __init__(self) -> None:
    super().__init__()

    QtGui.QFontDatabase.addApplicationFont('assets/super_creamy.ttf')
    QtGui.QFontDatabase.addApplicationFont('assets/comic_sans_ms.ttf')

    self.image_path = 'default'
    self.image_full = Image.new('RGB', (600, 600))
    self.image_shuffled = Image.new('RGB', (600, 600))
    self.image_array: list[Square] = []
    self.small_size = 0
    self.full_size = 600

    self.name = Name(self)
    self.title = Title(self)
    self.upload = Upload(self)
    self.randomize = Randomize(self)
    self.image_center = Image_center(self)
    self.count = Count(self)
    self.level = Level(self)
    self.leaderboard = Leaderboard(self)
    self.timer = Timer(self)
    self.source = Source(self)

    # .addWidget(y, x, hauteur, largeur)
    self.grid_big = QGridLayout()
    self.grid_big.addWidget(self.name, 1, 1, 1, 13)
    self.grid_big.addWidget(self.title, 2, 3, 1, 8)
    self.grid_big.addWidget(self.image_center, 3, 3, 8, 8)
    self.grid_big.addWidget(self.leaderboard, 4, 1, 6, 2)
    self.grid_big.addWidget(self.count, 5, 12, 1, 2)
    self.grid_big.addWidget(self.timer, 6, 12, 1, 2)
    self.grid_big.addWidget(self.level, 8, 12, 1, 2)
    self.grid_big.addWidget(self.randomize, 11, 3, 1, 4)
    self.grid_big.addWidget(self.upload, 11, 7, 1, 4)
    self.grid_big.addWidget(self.source, 11, 13, 1, 1)
    self.setLayout(self.grid_big)

    self.setWindowTitle('Sakura\'s Taquin')
    self.setMinimumSize(900, 800)
    self.setFont(QtGui.QFont('Comic Sans MS', 18))

    self.leaderboard.render()
    self.load_image()
    self.cut_image()


  def load_image(self) -> None:
    '''Load another image into the game'''

    # Fix wrong or default path
    if not path.isfile(self.image_path) or self.image_path == 'default':
      self.image_path = path.abspath('assets/sakura.png')

    # Change displayed title
    image_name = path.basename(self.image_path)
    self.title.change_title(image_name)
    
    # Open, crop then resize the image
    with Image.open(self.image_path) as im:
      la, lo = im.size
      center_x, center_y = la//2, lo//2
      size = min(la, lo)

      left = center_x - size//2
      top = center_y - size//2
      right = center_x + size//2
      bottom = center_y + size//2

      im = im.crop((left, top, right, bottom))
      im = im.resize((600, 600))

      self.image_full = im


  def cut_image(self) -> None:
    ''' Permet de couper l'image en n cases en fonction du level '''
    n = self.level.value()
    self.small_size = 600//n
    self.full_size = n * self.small_size
    self.image_array.clear()

    for i in range(n**2 - 1):
      x, y = i%n, i//n

      left = x * self.small_size
      top = y * self.small_size
      right = left + self.small_size
      bottom = top + self.small_size

      small_im = self.image_full.crop((left, top, right, bottom))
      sq = Square(small_im, x, y, x, y)
      self.image_array.append(sq)

    blank = Image.new('RGB', (self.small_size, self.small_size), '#000000')
    bl = Square(blank, n-1, n-1, n-1, n-1, is_blank=True)
    self.image_array.append(bl)

    self.randomize.randomize()


if __name__ == '__main__':
  ...
