from PySide6.QtWidgets import QTextEdit


class Level(QTextEdit):
  ''' Une case qui permet de choisir les dimensions  de la grille '''

  def __init__(self) -> None:
    super().__init__()
    self.model = None
    # self.value = None

  # def validate_input(self) -> bool:
  #   return self.toPlainText().isdigit() # permet de vérifier que ce qu'il y'a dans la case est un entier

