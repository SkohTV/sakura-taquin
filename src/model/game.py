from os import path

from PySide6 import QtGui
from PySide6.QtWidgets import QGridLayout, QWidget
from PIL import Image

from controller.level import Level
from controller.randomize import Randomize
from controller.square import Square
from controller.upload import Upload
from view.count import Count
from view.grid import Grid
from view.leaderboard import Leaderboard
from view.name import Name
from view.image_end import Image_end
from view.source import Source
from view.timer import Timer
from view.title import Title



class Game(QWidget):
  '''Core of game window'''

  def __init__(self) -> None:
    super().__init__()

    QtGui.QFontDatabase.addApplicationFont('assets/super_creamy.ttf')
    QtGui.QFontDatabase.addApplicationFont('assets/comic_sans_ms.ttf')

    self.image_path = 'default'
    self.image_full: Image.Image = None # type: ignore
    self.image_array: list[tuple[Square, int|None]] = []

    self.name = Name(self)
    self.title = Title(self)
    self.upload = Upload(self)
    self.randomize = Randomize(self)
    self.image_end = Image_end(self)
    self.grid = Grid(self)
    self.count = Count(self)
    self.level = Level(self)
    self.leaderboard = Leaderboard(self)
    self.timer = Timer(self)
    self.source = Source(self)

    # .addWidget(y, x, hauteur, largeur)
    self.grid_big = QGridLayout()
    self.grid_big.addWidget(self.name, 1, 1, 1, 13)
    self.grid_big.addWidget(self.title, 2, 3, 1, 8)
    # self.grid_big.addWidget(self.image_end, 3, 3, 8, 8)
    self.grid_big.addWidget(self.grid, 3, 3, 8, 8)
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
    self.image_end.set_image()
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
    for i in self.image_array:
      i[0].deleteLater()
    self.image_array.clear()
    self.grid.positions.clear()

    n = self.level.value()
    small_dim = 600//n


    for i in range(n**2 - 1):
      x, y = i%n, i//n

      left = x * small_dim
      top = y * small_dim
      right = left + small_dim
      bottom = top + small_dim

      small_im = self.image_full.crop((left, top, right, bottom))
      square = Square(self, small_im, small_dim)
      self.image_array.append((square, i))
      self.grid.add_image(square, x, y)


    blank = Image.new('RGB', (small_dim, small_dim), '#000000')
    blank_square = Square(self, blank, small_dim)
    self.image_array.append((blank_square, None))
    self.grid.add_image(blank_square, n-1, n-1)

    self.randomize.randomize()


    # self.grid = 2
    # self.image_array = []
    # self.full_image

    # self.level = Level()
    #cette ligne import l'attribut de la classe : level (de controller) dans modele
    # self.level.model = self


    # self.setLayout(self.grid)

  # def cut_image(self) -> None:
  #   ''' Permet de couper l'image en n cases en fonction du level '''
  #   n = self.level.value
  #   px = self.level.largeur
  #   largeur_img = px // n
  #   for i in range(n**2):
  #     coords = (i//n, i%n)
  #
  #     # largeur
  #     first_pixel = (coords[0]*largeur_img)
  #     last_pixel = first_pixel + largeur_img
  #
  #     # hauteur
  #     first_pixel = (coords[0]*largeur_img)
  #     last_pixel = first_pixel + largeur_img
  #
  # # la formule qui permet de récupérer les pixels de chaque morceau de l'image






if __name__ == '__main__':
  ...
