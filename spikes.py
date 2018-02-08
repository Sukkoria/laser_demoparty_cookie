# -*- coding: utf-8 -*-

from globalVars import *
import frame

class Spikes(object):
    def __init__(self, number, position, height, direction, color = 0xFFFFFF):
        self.number = number
        self.position = position
        self.height = height
        self.direction = direction # Horiz or vert
        self.color = color

        self.xy_list = []

    def SetColor(self, new_color):
        self.color = new_color
    
    def Compute(self):
        if (self.direction == "horiz"):
            self.width = screen_size[0]/self.number
            
            #self.xy_list.append((0, self.position))
            for i in range(self.number):
                self.xy_list.append((i*self.width, self.position))
                self.xy_list.append(((2*i+1)*self.width/2, self.position-self.height)) # Spiky thing
            self.xy_list.append((screen_size[0], self.position))
        elif (self.direction == "vert"):
            print("not yet implemented")

        else:
            print("No compatible direction found :'(")

    def Draw(self, f):
        f.PolyLineOneColor(self.xy_list, self.color) 


