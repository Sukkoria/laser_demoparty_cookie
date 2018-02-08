# -*- coding: utf-8 -*-

from globalVars import *
import frame

import random
import numpy

class Explode(object):
    def __init__(self, impact, direction, color = 0xFFFF00):
        self.impact = impact # Tuple
        self.color = color
        self.direction = direction

        random.seed()
        self.nbr_rays = random.randint(10, 30)
        self.xy_list = []

    def SetImpact(self, new_impact):
        self.impact = new_impact

    def SetColor(self, new_color):
        if (new_color == "random"):
            random.seed()
            new_color = colorshex[random.randint(0, len(colorshex)-1)]
        self.color = new_color

    def Compute(self):
        random.seed()
        self.nbr_rays = random.randint(10, 30)
        self.xy_list = []
        for i in range(self.nbr_rays):
            tmp_x = random.random()*(screen_size[0])
            tmp_y = random.random()*(screen_size[1])
            self.xy_list.append((tmp_x, tmp_y))
    def Draw(self, f):
        for xy in self.xy_list:
            f.Line(self.impact, xy, self.color)

