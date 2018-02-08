# -*- coding: utf-8 -*-

from globalVars import *

import random
import numpy

class Rainbow(object):
    def __init__(self, offset_y, role):
        self.nb_y = 10
        #self.nb_x = 9 # Seven colors
        self.color = colorshex
        self.nb_x = len(colorshex)
        self.offset_y = offset_y # In px from the top

        self.xy_list = []
        self.orig_xy_list = []

        self.role = role # Should be "floor", "ceiling", "rightwall" or "leftwall"
        if (self.role == "floor" or self.role == "ceiling"):
            self.orientation = "horiz"
            self.rel_offset_y =1.*self.offset_y/screen_size[1]
        elif (self.role == "rightwallobl" or self.role == "leftwallobl"):
            self.orientation = "obl"
        elif (self.role == "rightwall" or self.role == "leftwall"):
            self.orientation = "vert"
            self.rel_offset_y =1.*self.offset_y/screen_size[0]
    
        self.in_orig_state = True
        
    def Save(self):
        self.orig_xy_list = self.xy_list

    def SetColor(self, new_color):
        self.color = new_color

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
        if(self.orientation == "horiz"):
            for i in range(self.nb_x+1):
                increment_bott = screen_size[0]/self.nb_x 
                increment_up = self.rel_offset_y*screen_size[1]/self.nb_x
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

        elif (self.orientation == "obl"):
            for i in range(self.nb_x):
                increment = self.offset_y/self.nb_x
                if(i%2==0):
                    xy_list.append((self.offset_y + i*increment, 0))
                    xy_list.append((self.offset_y + i*increment, screen_size[0]))
                else:
                    xy_list.append((self.offset_y + i*increment, screen_size[0]))
                    xy_list.append((self.offset_y + i*increment, 0))

            for i in range(self.nb_y):
                increment_border = screen_size[1]/self.nb_y 
                increment_center = self.rel_offset_y*screen_size[1]/self.nb_y
                tmp_center = (self.rel_offset_y*screen_size[0], screen_size[1]/2 - (self.nb_y/2. - i)*increment_center)
                tmp_border = (i*increment_border, screen_size[1])
    
                if(i%2==0):
                    xy_list.append(tmp_border)
                    xy_list.append(tmp_center)
                else:
                    xy_list.append(tmp_center)
                    xy_list.append(tmp_border)


            if(self.role == "rightwallobl"):
                tmp_xy_list = []
                for xy in xy_list:
                    tmp_xy_list.append((
                        xy[0], xy[1]))
                self.xy_list = tmp_xy_list
            elif(self.role == "leftwallobl"):
                tmp_xy_list = []
                for xy in xy_list:
                    tmp_xy_list.append((
                        screen_size[0]- xy[0], xy[1]))
                self.xy_list = tmp_xy_list

        elif (self.orientation == "vert"):
            for i in range(self.nb_y+1):
                increment_border = screen_size[1]/self.nb_y 
                increment_center = self.rel_offset_y*screen_size[1]/self.nb_y
                tmp_center = (self.rel_offset_y*screen_size[0], screen_size[1]/2 - (self.nb_y/2. - i)*increment_center)
                tmp_border = (screen_size[0], i*increment_border)
    
                if(i%2==0):
                    xy_list.append(tmp_border)
                    xy_list.append(tmp_center)
                else:
                    xy_list.append(tmp_center)
                    xy_list.append(tmp_border)

            if(self.role == "rightwall"):
                tmp_xy_list = []
                for xy in xy_list:
                    tmp_xy_list.append((
                        xy[0], xy[1]))
                self.xy_list = tmp_xy_list
            elif(self.role == "leftwall"):
                tmp_xy_list = []
                for xy in xy_list:
                    tmp_xy_list.append((
                        screen_size[0]- xy[0], xy[1]))
                self.xy_list = tmp_xy_list


    def Draw(self, f):
        for i in range(0, len(self.xy_list), 2):
            try:
                f.Line(self.xy_list[i], self.xy_list[i+1], self.color[i/2])
                f.Line((self.xy_list[i][0]+10, self.xy_list[i][1]+10),(self.xy_list[i+1][0]+10, self.xy_list[i+1][1]+10), self.color[i/2])
            except:
                pass
            #print(i)
        #f.PolyLineOneColor(self.xy_list, 0xFFFFFF)

