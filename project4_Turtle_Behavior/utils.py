# This file includes the functions that used to judge, change the state of Mouse and Cat

from math import atan2, pi, pow, sqrt, acos, cos, sin, asin
from Vector import *

meter = 30.0

# Functions that deal with the movement of Mouse and Cat

    # if the cat is about to head to the statue, return its heading and speed
def catHeadToStatue(object):
    return atan2(200-object.position.x, object.position.y-200) * 180/pi, meter
    
    # if the cat is about to circulate, return its heading and speed    
def catCirculate(object):
    distance = sqrt(pow(object.position.x-200,2) + pow(object.position.y-200,2))
    head_angle  = atan2(200-object.position.x, object.position.y-200) * 180/pi
    round_angle =  1.25 * meter / distance * 180/pi
    delta_angle = 90 - round_angle/2

    speed = 2*distance*sin(1.25*meter/2/distance)

    return head_angle + delta_angle , speed

    # return mouse's heading and speed when it's circulating(as always).
def mouseCirculate(object):
    head_angle = atan2(200-object.position.x, object.position.y-200) * 180/pi
    round_angle = meter / 40.0 * 180/pi
    delta_angle = 90 - round_angle/2.0
    speed =2*(meter+10)*sin(3.0/8.0)
    return head_angle + delta_angle, speed


# Functions that judge the states of Cat and Mouse.

    # to verify whether the cat see the mouse, return True or False
def catSeeMouse(cat, mouse):
    catRadius = sqrt(pow(cat.position.x-200,2) + pow(cat.position.y-200,2))
    mouseAngle = atan2(mouse.position.x-200, 200-mouse.position.y)
    catAngle = atan2(cat.position.x-200, 200-cat.position.y)
    return catRadius * cos(catAngle - mouseAngle) >= 1.0 

    # to avoid the cat goes into the statue. If it is about to do it, move it back to the boundary of statue
def intoTheStatue(object):
    distance = sqrt(pow(object.position.x-200,2) + pow(object.position.y-200,2))
    angle = atan2(200-object.position.x, object.position.y-200) 
    if distance >= 2*meter : 
        return object.position + unit(object.heading) * object.speed
    else:
        print "boundary"
        return Vector(200 - meter * sin(angle), 200 + meter * cos(angle))

    # To verify whether the cat catches the mouse, based on the angle of mouse and cat. 
def catCatchMouse(cat, cat_old_heading, mouse_heading):
    cat_old_angle = cat_old_heading * pi/180   
    cat_new_angle = cat.heading * pi/180
    mouse_angle   = mouse_heading * pi/180
    atTheBase = sqrt(pow(cat.position.x-200,2) + pow(cat.position.y-200,2)) <= 30.1
    if atTheBase and (cos(mouse_angle - cat_old_angle) > cos(cat_new_angle - cat_old_angle)) and (cos(cat_new_angle - mouse_angle) > cos(cat_new_angle - cat_old_angle)) :
        print "Catch!!!!!!!!"
        return True
    else:
        return False

    
