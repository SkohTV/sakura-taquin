from PySide6 import QtGui
from PySide6.QtWidgets import QWidget
from PIL import Image

from controller.level import Level


class Game(QWidget):
  '''Core of game window'''

  def __init__(self) -> None:
    super().__init__()
    # self.grid = 2
    # self.image_array = []
    # self.full_image

    # self.level = Level()
    #cette ligne import l'attribut de la classe : level (de controller) dans modele
    # self.level.model = self

    # self.setLayout(self.grid)
    self.setWindowTitle('Sakura\'s Taquin')
    self.setMinimumSize(300, 400)
    self.setFont(QtGui.QFont('Arial', 18))

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
