from maze.gui import Gui
from maze.text import Text
from maze.game import Game


def build(window, title, message, canvas, clicked=False, outline_width=1,
          running=False):
    Gui.rectangle(window,
                  width=Game.side * 3 / 4 + outline_width * 2,
                  height=Game.side / 8 + outline_width,
                  x=Game.side / 8 - outline_width,
                  y=Game.side / 8 - outline_width,
                  outline_width=outline_width)
    Gui.rectangle(window,
                  width=Game.side * 3 / 4 + outline_width * 2,
                  height=Game.side / 2 + outline_width * 2,
                  x=Game.side / 8 - outline_width,
                  y=Game.side / 4 - outline_width,
                  outline_width=outline_width)
    Gui.rectangle(window,
                  width=Game.side * 3 / 4 + outline_width * 2,
                  height=Game.side / 8 + outline_width,
                  x=Game.side / 8 - outline_width,
                  y=Game.side * 3 / 4,
                  outline_width=outline_width,
                  message=message,
                  font_color=(0, 0, 0),
                  size_ratio=1/2)
    Text.display(window, title, font_size=Game.side/16,
                 center_y=Game.side*3/16)
    if running:
        Gui.rectangle(window,
                      width=Game.side * 5 / 32,
                      height=Game.side * 5 / 128,
                      x=Game.side * 9 / 64,
                      y=Game.side * 9 / 64,
                      color=(30, 30, 30),
                      font_color=(50, 50, 50),
                      outline=False,
                      message="Clear")
        Gui.rectangle(window,
                      width=Game.side * 5 / 32,
                      height=Game.side * 5 / 128,
                      x=Game.side * 9 / 64,
                      y=Game.side * 3 / 16,
                      color=(50, 50, 50),
                      hover_color=(100, 100, 100),
                      clicked=clicked,
                      on_click=canvas.stop,
                      outline=False,
                      message="Cancel")
    else:
        Gui.rectangle(window,
                      width=Game.side * 5 / 32,
                      height=Game.side * 5 / 128,
                      x=Game.side * 9 / 64,
                      y=Game.side * 9 / 64,
                      color=(50, 50, 50),
                      hover_color=(100, 100, 100),
                      clicked=clicked,
                      on_click=canvas.clear,
                      outline=False,
                      message="Clear")
        Gui.rectangle(window,
                      width=Game.side * 5 / 32,
                      height=Game.side * 5 / 128,
                      x=Game.side * 9 / 64,
                      y=Game.side * 3 / 16,
                      color=(50, 50, 50),
                      hover_color=(100, 100, 100),
                      clicked=clicked,
                      on_click=canvas.run,
                      outline=False,
                      message="Run")
