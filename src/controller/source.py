# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

import webbrowser
from PySide6.QtWidgets import QPushButton


class Source(QPushButton):
  '''Affiche la duree entre le premier et le dernier coups'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.clicked.connect(self.on_click)
    self.setFixedSize(50, 50)
    self.setStyleSheet('border-image: url(assets/github.png) 0 0 0 0 strech strech')

  def on_click(self) -> None:
    webbrowser.open('https://github.com/SkohTV/sakura-taquin')

  # def change_title(self, title1: str) -> None:
  #   self.setText(title1)
