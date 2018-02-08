# -*- coding: utf-8 -*-

from globalVars import *

import random
import numpy

class Grid(object):
    def __init__(self, offset_y, role):
        self.nb_y = 10
        self.nb_x = 9 # Must be odd !

        self.offset_y = offset_y # In px from the top
        self.rel_offset_y =1.*self.offset_y/screen_size[1]

        self.xy_list = []
        self.orig_xy_list = []

        self.role = role # Should be "floor", "ceiling", "rightwall" or "leftwall"

        self.in_orig_state = True
        
    def Save(self):
        self.orig_xy_list = self.xy_list

    def Restore(self):
        self.xy_list = self.orig_xy_list
        self.in_orig_state = True

    def Rotate(self, angle): # Angle has to be given in rad
        self.in_orig_state = False
        self.Save()
        xy_list = []
        for point in self.xy_list:
            print(point)
            r = numpy.sqrt(numpy.power(point[0], 2) + numpy.power(point[1], 2))
            xy_list.append((r*numpy.cos(angle), r*numpy.sin(angle)))

        self.xy_list = xy_list
    def Compute(self):
        xy_list = []
        for i in range(self.nb_y):
            increment = self.offset_y/self.nb_y
            if(i%2==0):
                xy_list.append((0, self.offset_y + i*increment))
                xy_list.append((screen_size[0], self.offset_y + i*increment))
            else:
                xy_list.append((screen_size[0], self.offset_y + i*increment))
                xy_list.append((0, self.offset_y + i*increment))

        for i in range(self.nb_x+1):
            increment_bott = screen_size[0]/self.nb_x 
            increment_up = self.rel_offset_y*screen_size[1]/self.nb_x
            if(i<self.nb_x/2.):
                tmp_up = (screen_size[0]/2 - (self.nb_x/2. - i)*increment_up, self.rel_offset_y*screen_size[1])
            elif(i==self.nb_x/2.):
                tmp_up = (screen_size[0]/2 - (self.nb_x/2. - i)*increment_up, self.rel_offset_y*screen_size[1])
            else:
                tmp_up = (screen_size[0]/2 - (self.nb_x/2. - i)*increment_up, self.rel_offset_y*screen_size[1])



            tmp_bott = (i*increment_bott, screen_size[1])

            if(i%2==0):
                xy_list.append(tmp_bott)
                xy_list.append(tmp_up)
            else:
                xy_list.append(tmp_up)
                xy_list.append(tmp_bott)

        if(self.role == "floor"):
            self.xy_list = xy_list
        elif(self.role == "ceiling"):
            tmp_xy_list = []
            for xy in xy_list:
                tmp_xy_list.append((
                        xy[0], screen_size[1]-xy[1]))
            self.xy_list = tmp_xy_list
        elif(self.role == "rightwall"):
            tmp_xy_list = []
            for xy in xy_list:
                tmp_xy_list.append((
                    screen_size[0]*xy[1]/screen_size[1], screen_size[0]*xy[0]/screen_size[1])) 
            self.xy_list = tmp_xy_list
        elif(self.role == "leftwall"):
            tmp_xy_list = []
            for xy in xy_list:
                tmp_xy_list.append((
                    screen_size[0]*(1-xy[1]/screen_size[1]), screen_size[0]*xy[0]/screen_size[1])) 
            self.xy_list = tmp_xy_list


    def Draw(self, f):
        f.PolyLineOneColor(self.xy_list, 0xFFFFFF)

