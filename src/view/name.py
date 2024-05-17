from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QLabel


class Name(QLabel):
  '''On affiche le nom de notre jeu : "The Sakura's Taquin game"'''

  def __init__(self, model) -> None:
    super().__init__()
    self.model = model
    self.setText('The Sakura\'s Taquin Game')
    self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    self.setFont(QtGui.QFont('Super Creamy', 36))

    # Ajoute d'une police custom

    #self.setStyleSheet()
