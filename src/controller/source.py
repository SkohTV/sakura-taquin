# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

import webbrowser
from PySide6.QtWidgets import QPushButton



class Source(QPushButton):
  '''Open a link with the source code'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.clicked.connect(self.on_click)
    self.setFixedSize(50, 50)
    self.setStyleSheet('border-image: url(assets/github.png) 0 0 0 0 strech strech') # Show the github logo on the button


  def on_click(self) -> None:
    '''Open the url in a new tab'''
    webbrowser.open('https://github.com/SkohTV/sakura-taquin')
