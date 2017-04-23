from Turtle import Turtle
from Vector import *
from Color import *
from utils import *

class Mouse(Turtle):       #### Inherit behavior from Turtle
    """This turtle walks in a straight line forever."""

    def __init__(self, position, heading, speed, fill=blue, stop=0, **style):
        Turtle.__init__(self, position, heading, fill=fill,  **style)
        self.speed = speed
        self.stop = stop	
        self.catched = 0
    def getnextstate(self,mouse):
        """Advance straight ahead."""

        if (self.catched == 0):                                 # If the Mouse is catches, stop.
            self.heading, self.speed = mouseCirculate(self)
        else:                                                   # Or it will just circulate
            self.heading, self.speed = 0,0
 
        return self.position + unit(self.heading)*self.speed, self.heading

    def getshape(self):
        forward = unit(self.heading)
        right   = unit(self.heading + 90)
       
        return [self.position + forward * 5,
                self.position - right * 5,
                self.position + right * 5,
                self.position - forward * 5]
