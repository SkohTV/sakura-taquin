from PySide6 import QtCore
from PySide6.QtWidgets import QLabel


class Title(QLabel):
  '''Le titre change en fonction de l'image mise dans la grille '''

  def __init__(self, model) -> None:
    super().__init__()
    self.model = model
    self.setText('Hello')
    self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

  # def change_title(self, title1: str) -> None:
  #   self.setText(title1)
