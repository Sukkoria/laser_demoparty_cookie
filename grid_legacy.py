# -*- coding: utf-8 -*-

from globalVars import *

import random
import numpy

class Grid(object):
    def __init__(self, offset_y):
        self.nb_y = 10
        self.nb_x = 9 # Must be odd !

        self.offset_y = offset_y # In px from the top
        self.rel_offset_y =1.*self.offset_y/screen_size[1]

    def Draw(self, f):
        xy_list = []
        #xy_list.append((0, self.offset_y))
        #xy_list.append((screen_size[0], self.offset_y))
        for i in range(self.nb_y):
            increment = self.offset_y/self.nb_y
            if(i%2==0):
                xy_list.append((0, self.offset_y + i*increment))
                xy_list.append((screen_size[0], self.offset_y + i*increment))
            else:
                xy_list.append((screen_size[0], self.offset_y + i*increment))
                xy_list.append((0, self.offset_y + i*increment))

        for i in range(self.nb_x):
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
            #print(xy_list[self.nb_y+i])

        #print(xy_list)

        f.PolyLineOneColor(xy_list, 0xFFFFFF)

