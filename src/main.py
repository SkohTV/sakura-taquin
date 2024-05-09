from PySide6.QtWidgets import QApplication
from model.game import Game


if __name__ == "__main__":
  print('Hello world')
  app = QApplication()
  game = Game()
  game.show()
  app.exec()

