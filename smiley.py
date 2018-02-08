# -*- coding: utf-8 -*-

from globalVars import *

class Smiley(object):
    def __init__(self, skin, offset=(screen_size[0]/2, screen_size[1]/2), zoom = 250):
        self.skin = skin
        self.offset = offset
        self.zoom = zoom

        self.color = 0xFF0000

    def Draw(self, f):
        if(self.skin == "devil"):
            # Eyebrows
            xy_list = []

            xy_list.append((
                self.offset[0] - 1*self.zoom,
                self.offset[1] - 0.95*self.zoom))
            xy_list.append((
                self.offset[0] - 0.5*self.zoom,
                self.offset[1] - 1.05*self.zoom))
            xy_list.append((
                self.offset[0] - 0.25*self.zoom,
                self.offset[1] - 0.85*self.zoom))

            xy_list_reverse = []
            for xy in xy_list[::-1]:
                new_x = 2*self.offset[0]-xy[0]
                new_y = xy[1]
                xy_list_reverse.append((new_x, new_y))
            f.PolyLineOneColor(xy_list, self.color)
            f.PolyLineOneColor(xy_list_reverse, self.color)

            # 3 Eyes : 
            xy_list = []
            # Left one 
            xy_list.append((
                self.offset[0] - 0.55*self.zoom, 
                self.offset[1] - 0*self.zoom))
            xy_list.append((
                self.offset[0] - 0.55*self.zoom, 
                self.offset[1] - 0.75*self.zoom))
            # Middle one
            xy_list.append((
                self.offset[0] + 0*self.zoom, 
                self.offset[1] - 0*self.zoom))
            xy_list.append((
                self.offset[0] + 0*self.zoom, 
                self.offset[1] - 0.75*self.zoom))
            # Right one 
            xy_list.append((
                self.offset[0] + 0.55*self.zoom, 
                self.offset[1] - 0*self.zoom))
            xy_list.append((
                self.offset[0] + 0.55*self.zoom, 
                self.offset[1] - 0.75*self.zoom))

            for i in range(3):
                f.Line(xy_list[2*i], xy_list[2*i+1], self.color)

            # Mouth and teeth
            xy_list = []
            xy_list.append((
                self.offset[0] - 0.9*self.zoom,
                self.offset[1] - 0*self.zoom))
            xy_list.append((
                self.offset[0] - 0.75*self.zoom,
                self.offset[1] + 0.25*self.zoom))
            xy_list.append((
                self.offset[0] - 0.75*self.zoom,
                self.offset[1] + 0.9*self.zoom))
            xy_list.append((
                self.offset[0] - 0.5*self.zoom,
                self.offset[1] + 0.4*self.zoom))
            xy_list.append((
                self.offset[0] - 0.4*self.zoom,
                self.offset[1] + 0.45*self.zoom))
            xy_list.append((
                self.offset[0] - 0.25*self.zoom,
                self.offset[1] + 0.5*self.zoom))
            xy_list.append((
                self.offset[0] - 0.1*self.zoom,
                self.offset[1] + 0.55*self.zoom))
            xy_list_reverse = []
            for xy in xy_list[::-1]:
                new_x = 2*self.offset[0]-xy[0]
                new_y = xy[1]
                xy_list_reverse.append((new_x, new_y))
            xy_list = xy_list + xy_list_reverse
            f.PolyLineOneColor(xy_list, self.color)

        elif(self.skin == "nice"):
            # 3 Eyes : 
            xy_list = []
            # Left one 
            xy_list.append((
                self.offset[0] - 0.55*self.zoom, 
                self.offset[1] - 0*self.zoom))
            xy_list.append((
                self.offset[0] - 0.55*self.zoom, 
                self.offset[1] - 0.75*self.zoom))
            # Middle one
            xy_list.append((
                self.offset[0] + 0*self.zoom, 
                self.offset[1] - 0*self.zoom))
            xy_list.append((
                self.offset[0] + 0*self.zoom, 
                self.offset[1] - 0.75*self.zoom))
            # Right one 
            xy_list.append((
                self.offset[0] + 0.55*self.zoom, 
                self.offset[1] - 0*self.zoom))
            xy_list.append((
                self.offset[0] + 0.55*self.zoom, 
                self.offset[1] - 0.75*self.zoom))

            for i in range(3):
                f.Line(xy_list[2*i], xy_list[2*i+1], self.color)

