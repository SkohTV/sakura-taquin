from datetime import timedelta
from collections import namedtuple
from PySide6 import QtCore
from PySide6.QtWidgets import QLabel


Score = namedtuple('Score', 'level moves time')


class Leaderboard(QLabel):
  '''Affiche les meilleurs scores'''

  def __init__(self, model) -> None:
    super().__init__()
    self.model = model
    self.scores: list[Score] = []

    # trash values
    self.score = [
      Score(3, 3, timedelta(minutes=3, seconds=2)),
      Score(2, 3, timedelta(minutes=1, seconds=20)),
      Score(3, 1, timedelta(minutes=0, seconds=45))
    ]

  def add(self, level: int, moves: int, time: timedelta) -> None:
    new_score = Score(level, time, moves)
    self.scores.append(new_score)

  def render(self) -> None:
    sorted(self.scores)
    text = ''
    for i in self.scores:
      text += f'{i.level} - {i.moves} - {i.time}\n'
    self.setText(text)

