# This file is the main driver of the procedure, including the TKinter, Arena and instance of Statue, Mouse, Cat classes.

from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from WalkingTurtle  import WalkingTurtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector
from Statue  import Statue
from Mouse   import Mouse
from Cat     import Cat
from utils   import *

meter = 30

    # Tkinter instantiation.

tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk)                      # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen

    # define the initial position of statue, mouse and cat.

statue_position_x   = 200
statue_position_y   = 200
mouse_position_x    = 230
mouse_position_y    = 200
cat_position_x      = 350
cat_position_y      = 200

    # instantiate Statue, Mouse and Cat classes.

statue  = Statue(Vector(statue_position_x, statue_position_y), 0)
mouse   = Mouse(Vector(mouse_position_x, mouse_position_y), 196.4576, meter)
cat     = Cat(Vector(cat_position_x, cat_position_y), 0, 1.25*meter)

    # Add these instances into the Arena.

arena.add(statue)	                   # Add a fixed statue
arena.add(mouse)                       # Add a stupid mouse that will circulate around the statue
arena.add(cat)                         # Add a cat that manage to catch the mouse, it has 2 strategy to move

tk.mainloop()                          # Enter the Tkinter event loop

