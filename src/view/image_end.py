from PySide6.QtWidgets import QLabel


class Image_end(QLabel):
  '''Blablabla'''

  def __init__(self, model) -> None:
    super().__init__()
    self.model = model

  def set_image(self) -> None:
    self.setPixmap(self.model.image_full.scaled(500, 500))

