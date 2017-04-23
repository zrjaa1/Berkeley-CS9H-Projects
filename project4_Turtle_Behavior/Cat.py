# This file defines the behavior of Cat.

from Turtle import Turtle
from Vector import *
from Color import *
from utils import *
from math import pi, sqrt, pow

circulate = 0
head = 1
meter = 30.0

class Cat(Turtle):       #### Inherit behavior from Turtle
    """This turtle walks in a straight line forever."""

    def __init__(self, position, heading, speed, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed
        self.catch = 0

        # this method will first judge the state of Cat, then deal with its movement.
    def getnextstate(self,mouse):

        previous_heading = self.heading
        distance = sqrt(pow(self.position.x-200,2) + pow(self.position.y-200,2))    # distance between statue and Cat
 
        if (distance <= 30.1):                                                      # The distance will not be perfectly 30.
            atTheBase = True
        else :
            atTheBase = False

        if catSeeMouse(self, mouse):                                                # If the cat sees the mouse, it moves heading to statue 
            self.state = head
        else:
            self.state = circulate                                                  # If not, just circulating

        if self.catch == 1:                                                         # If the Cat catches the Mouse, stop
            self.heading, self.speed = 0,0
            self.state = circulate    
        
        elif atTheBase:                                               # If the Cat is already at the base of statue, it keeps circulating.
            self.heading, self.speed = catCirculate(self)
            self.state = circulate
            print 'at the base, continue circulating'

        elif self.state == head:                                      # If not at the base, move head to statue or just circulate
            self.heading, self.speed = catHeadToStatue(self)
            print 'head to statue'

        elif self.state == circulate:
            self.heading, self.speed = catCirculate(self)
            print 'circulate'

        if catCatchMouse(self, previous_heading, mouse.heading):                 # Judge catch based on previous and present states.        
            self.catch = 1
            mouse.catched = 1

        if self.state == head:                                             # If the cat is heading to statue, avoid it goes into the statue.
            return intoTheStatue(self), self.heading

        else:
            return self.position + unit(self.heading) * self.speed, self.heading
