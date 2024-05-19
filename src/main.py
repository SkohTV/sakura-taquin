from PySide6 import QtGui
from PySide6.QtWidgets import QApplication
from model.game import Game


if __name__ == "__main__":
  app = QApplication()
  game = Game()
  app.setFont(QtGui.QFont('Comic Sans MS', 18))
  game.show()
  app.exec()

