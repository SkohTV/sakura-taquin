# Circular reference import solving
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from model.game import Game

from PySide6 import QtCore
from PySide6.QtWidgets import QLabel



class Timer(QLabel):
  '''Display time elapsed since first move'''

  def __init__(self, model: Game) -> None:
    super().__init__()
    self.model = model
    self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    # Create a timer to auto update time
    self.current_time = 0.00
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.update_time)


  def start(self) -> None:
    '''Start the timer'''
    if not self.timer.isActive():
      self.timer.start(10)


  def stop(self) -> None:
    '''Stop the timer'''
    if self.timer.isActive():
      self.timer.stop()


  def reset(self) -> None:
    '''Reset the timer'''
    self.stop()
    self.current_time = 0.00
    self.setText('-.-- s')


  def update_time(self) -> None:
    '''Add 0.01 to the time displayed (every 0.01s)'''
    self.current_time += 0.01
    self.setText(f'{self.current_time:.2f} s')
