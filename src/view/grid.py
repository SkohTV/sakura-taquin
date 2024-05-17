from PySide6.QtWidgets import QGridLayout


class Grid(QGridLayout):
  '''Blablabla'''

  def __init__(self, model) -> None:
    super().__init__()
    self.model = model
