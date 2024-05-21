from os import path
from dataclasses import dataclass

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QGridLayout, QMainWindow, QWidget
from PIL import Image

from controller.level import Level
from controller.randomize import Randomize
from controller.upload import Upload
from view.count import Count
from view.image_center import Image_center
from view.leaderboard import Leaderboard
from view.name import Name
from controller.source import Source
from view.timer import Timer
from view.title import Title



# Create a small class to store informations about an image
@dataclass
class Square:
  im: Image.Image # The image object
  true_x: int # The correct x pos of the image
  true_y: int # The correct y pos
  current_x: int # The current x pos
  current_y: int # The current y pos
  is_blank: bool = False # If the image is blank or not


class Game(QMainWindow):
  '''Core of game window'''

  def __init__(self) -> None:
    super().__init__()

    # Create a widget as main widget to force user focus on THIS widget
    self.widget = QWidget()
    self.setCentralWidget(self.widget)
    self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

    # Add fonts
    QtGui.QFontDatabase.addApplicationFont('assets/super_creamy.ttf')
    QtGui.QFontDatabase.addApplicationFont('assets/comic_sans_ms.ttf')

    # Creation of variables to stock image values
    self.image_path = 'default'
    self.image_full = Image.new('RGB', (600, 600))
    self.image_shuffled = Image.new('RGB', (600, 600))
    self.image_array: list[Square] = []
    self.small_size = 0
    self.full_size = 600
    self.game = False

    # Store widgets in variables
    self.name = Name(self)
    self.title = Title(self)
    self.upload = Upload(self)
    self.randomize = Randomize(self)
    self.image_center = Image_center(self)
    self.count = Count(self)
    self.level = Level(self)
    self.leaderboard = Leaderboard(self)
    self.timer = Timer(self)
    self.source = Source(self)

    # Place widgets on layout and add layout to window
    # .addWidget(y, x, hauteur, largeur)
    self.grid_big = QGridLayout()
    self.grid_big.addWidget(self.name, 1, 1, 1, 13)
    self.grid_big.addWidget(self.title, 2, 3, 1, 8)
    self.grid_big.addWidget(self.image_center, 3, 3, 8, 8)
    self.grid_big.addWidget(self.leaderboard, 4, 1, 6, 2)
    self.grid_big.addWidget(self.count, 5, 12, 1, 2)
    self.grid_big.addWidget(self.timer, 6, 12, 1, 2)
    self.grid_big.addWidget(self.level, 8, 12, 1, 2)
    self.grid_big.addWidget(self.randomize, 11, 3, 1, 4)
    self.grid_big.addWidget(self.upload, 11, 7, 1, 4)
    self.grid_big.addWidget(self.source, 11, 13, 1, 1)
    self.widget.setLayout(self.grid_big)

    # Set window parameters
    self.setWindowTitle('Sakura\'s Taquin')
    self.setMinimumSize(900, 800)
    self.setFont(QtGui.QFont('Comic Sans MS', 18))

    # Load the image and prepare the game
    self.leaderboard.render()
    self.load_image()
    self.cut_image()


  def load_image(self) -> None:
    '''Load another image into the game'''

    # Fix wrong or default path
    if not path.isfile(self.image_path) or self.image_path == 'default':
      self.image_path = path.abspath('assets/sakura.png')

    # Change displayed title
    image_name = path.basename(self.image_path)
    self.title.change_title(image_name)
    
    # Open, crop then resize the image
    with Image.open(self.image_path) as im:
      la, lo = im.size
      center_x, center_y = la//2, lo//2
      size = min(la, lo)

      left = center_x - size//2
      top = center_y - size//2
      right = center_x + size//2
      bottom = center_y + size//2

      # Convert full size image to 600x600 image
      im = im.crop((left, top, right, bottom))
      im = im.resize((600, 600))

      self.image_full = im # Store the image


  def cut_image(self) -> None:
    ''' Permet de couper l'image en n cases en fonction du level '''

    # Reset old image stored values
    n = self.level.value()
    self.small_size = 600//n
    self.full_size = n * self.small_size
    self.image_array.clear()

    # Loop as many times as there are images
    # To generate small images
    for i in range(n**2 - 1):
      x, y = i%n, i//n # Compute x and y of current small image

      left = x * self.small_size
      top = y * self.small_size
      right = left + self.small_size
      bottom = top + self.small_size

      # Create small image square (image + position now + position correct) from big image
      small_im = self.image_full.crop((left, top, right, bottom))
      sq = Square(small_im, x, y, x, y)
      self.image_array.append(sq) # Store images in image_array

    # Also create a blank small square
    blank = Image.new('RGBA', (self.small_size, self.small_size), (0, 0, 0, 0))
    bl = Square(blank, n-1, n-1, n-1, n-1, is_blank=True)
    self.image_array.append(bl)

    # Randomize the squares
    self.randomize.randomize()


  def full_check(self) -> bool:
    '''Check if all images are in the correct position'''
    for i in self.image_array:
      if not i.current_x == i.true_x or not i.current_y == i.true_y:
        return False
    return True



  def move_img(self, dir: str, render = True) -> bool:
    '''Move an image to the blank spot'''

    # Get the blank spot
    blank = self.image_array[-1]

    # Get coordinates of case next to blank spot, depending on key pressed
    if dir == 'up' and not blank.current_y == 0:
        case = blank.current_x, blank.current_y - 1

    elif dir == 'down' and not blank.current_y == self.level.value() - 1:
        case = blank.current_x, blank.current_y + 1

    elif dir == 'left' and not blank.current_x == 0:
        case = blank.current_x - 1, blank.current_y

    elif dir == 'right' and not blank.current_x == self.level.value() - 1:
        case = blank.current_x + 1, blank.current_y

    else: # Move not allowed
      return False

    # Find the case corresponding to coordinates and change them to the blank coordinates
    for i in self.image_array:
      if i.current_x == case[0] and i.current_y == case[1]:
        i.current_x, i.current_y = blank.current_x, blank.current_y

    # Set blank coordinates to selected case coordinates
    blank.current_x, blank.current_y = case

    # Stop here if we are doing a randomizing
    if not render:
      return True

    # Regenerate image
    self.image_center.generate_image()

    # If first move, start the game
    if self.count.count == 0:
      self.timer.start()

    # Add one to the counter
    self.count.add()

    # If finished, then end
    if self.full_check():
      self.stop_game()

    return True


  def stop_game(self) -> None:
    '''Stop the game'''

    self.timer.stop()
    self.leaderboard.add(level=self.level.value(), moves=self.count.count, time=self.timer.current_time)
    self.leaderboard.render()
    self.image_center.final_image()
    self.game = False


  def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
    '''Function called automatically on key press'''
    if not self.game: # If game is not running (full image), do nothing
      return

    # Get readable names for keys
    down = QtCore.Qt.Key.Key_Down
    up = QtCore.Qt.Key.Key_Up
    left = QtCore.Qt.Key.Key_Left
    right = QtCore.Qt.Key.Key_Right

    # Get pressed key
    key = event.key()

    # Match key pressed to square movement
    if key == down:
      self.move_img('up')
    elif key == up:
      self.move_img('down')
    elif key == right:
      self.move_img('left')
    elif key == left:
      self.move_img('right')

