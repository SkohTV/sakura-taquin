# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from collections import namedtuple

from PySide6 import QtCore
from PySide6.QtWidgets import QLabel


Score = namedtuple('Score', 'level moves time')


class Leaderboard(QLabel):
  '''Affiche les meilleurs scores'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.scores: list[Score] = []
    self.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
    self.setStyleSheet('font-size: 18px')


  def add(self, level: int, moves: int, time: float) -> None:
    new_score = Score(level, moves, time)
    self.scores.append(new_score)


  def render(self) -> None:
    sorted(self.scores)
    text = '<b>----- Leaderboard -----</b><br>'

    if not self.scores:
      text += '<i>Aucun score...</i>'
    for i in self.scores:
      text += f'{i.level}x{i.level} - {i.moves} coups - {i.time:.2f} s<br>'

    self.setText(text)

