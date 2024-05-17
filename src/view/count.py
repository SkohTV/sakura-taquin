from PySide6 import QtCore
from PySide6.QtWidgets import QLabel


class Count(QLabel):
  '''Compte le nombre de coups jouees'''

  def __init__(self, model) -> None:
    super().__init__()
    self.model = model
    self.setText('0')
    self.count = 0
    self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

  def add(self) -> None:
    self.count += 1
    self.setText(str(self.count))

  def reset(self) -> None:
    self.count = 0
    self.setText('0')
