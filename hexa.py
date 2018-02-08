# -*- coding: utf-8 -*-

from globalVars import *
import frame

import random
import numpy

class Hex(object):
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.xy_list = []
        self.angles = [0, numpy.pi/3, numpy.pi*2/3, numpy.pi, -numpy.pi*2/3, -numpy.pi/3, 0]

    def Draw(self, f):
        for angle in angles:
            self.xy_list.append(
                    (self.size*numpy.cos(angle), self.size*numpy.sin(angle)))

        f.PolyLineOneColor(self.xy_list, self.color)
