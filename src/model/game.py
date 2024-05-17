from os import path

from PySide6 import QtGui
from PySide6.QtWidgets import QGridLayout, QWidget
from PIL import Image
from PIL.ImageQt import ImageQt
from controller.level import Level

from controller.upload import Upload

from view.count import Count
from view.leaderboard import Leaderboard
from view.name import Name
from view.image_end import Image_end
from view.title import Title



class Game(QWidget):
  '''Core of game window'''

  def __init__(self) -> None:
    super().__init__()

    QtGui.QFontDatabase.addApplicationFont('assets/super_creamy.ttf')
    self.setFont(QtGui.QFont('Comic Sans MS', 18))

    self.image_path = 'default'
    self.image_full: QtGui.QPixmap = None # type: ignore
    self.image_array = []

    self.name = Name(self)
    self.title = Title(self)
    self.upload = Upload(self)
    self.image_end = Image_end(self)
    self.count = Count(self)
    # self.level = Level(self)
    self.leaderboard = Leaderboard(self)
    self.leaderboard.render()

    # .addWidget(x, y, hauteur, largeur)
    self.grid_big = QGridLayout()
    self.grid_big.addWidget(self.name)
    self.grid_big.addWidget(self.title)
    self.grid_big.addWidget(self.upload)
    self.grid_big.addWidget(self.image_end)
    self.grid_big.addWidget(self.count)
    # self.grid_big.addWidget(self.level)
    self.grid_big.addWidget(self.leaderboard)
    self.setLayout(self.grid_big)

    self.setWindowTitle('Sakura\'s Taquin')
    self.setMinimumSize(900, 700)
    self.setFont(QtGui.QFont('Arial', 18))


  def load_image(self) -> None:
    print(self.image_path)
    if not path.isfile(self.image_path) or self.image_path == 'default':
      self.image_path = path.abspath('assets/sakura.png')
    
    with Image.open(self.image_path) as im:
      la, lo = im.size
      center_x, center_y = la//2, lo//2
      size = min(la, lo)

      left = center_x - size//2
      top = center_y - size//2
      right = center_x + size//2
      bottom = center_y + size//2

      im = im.crop((left, top, right, bottom))
      self.image_full = QtGui.QPixmap.fromImage(ImageQt(im))


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
