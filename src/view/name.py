from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFontDatabase, QFont


class Name(QLabel):
  '''On affiche le nom de notre jeu : "The Sakura's Taquin game"'''

  def __init__(self) -> None:
    super().__init__()
    self.model = None
    self.setText('The Sakura\'s Taquin Game')

    # Ajoute d'une police custom
    # QFontDatabase.addApplicationFont('assets/police.ttf')
    # self.setFont(QFont('Super Creamy', 18))

    #self.setStyleSheet()
