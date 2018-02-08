# -*- coding: utf-8 -*-

from globalVars import *
import frame

import random
import numpy

# TO DO : Define other clouds as tetriminoes
POINTS_T = [(-1.5,0), (-0.5, 0), 
        (-0.5, -1), (0.5, -1), 
        (0.5, 0), (1.5, 0), 
        (1.5, 1), (0.5, 1), 
        (-0.5, 1), (-1.5, 1), (-1.5, 0)]
POINTS_I = [(-1, 0.25), (1,0.25), (1, -0.25), (-1, -0.25), (-1, 0.25)]

class Clouds(object):
    def __init__(self, position, zoom, cloud_type, color = 0x00BBBB):
        self.position = position # Tuple
        self.zoom = zoom
        self.color = color
        self.cloud_type = cloud_type
        if (self.cloud_type == "I"):
            self.ref_cloud = POINTS_I
        elif(self.cloud_type == "T"):
            self.ref_cloud = POINTS_T
            #self.ref_cloud = POINTS_I

        self.xy_list = []
        self.xy_list_rain = []

    def SetPosition(self, new_position):
        self.position = new_position

    def SetColor(self, new_color):
        self.color = new_color

    def Compute(self):
        self.xy_list = []
        for i in range(len(self.ref_cloud)):
            self.xy_list.append((
                self.position[0] + self.ref_cloud[i][0]*self.zoom, 
                self.position[1] + self.ref_cloud[i][1]*self.zoom))

    def ComputeRain(self):
        self.xy_list_rain = []
        random.seed()
        for i in range(len(self.xy_list)*2):
            tmp_x = random.randint(0, self.zoom) + self.position[0]
            tmp_y = random.randint(10, screen_size[1]) + self.position[1]
            tmp_y_2 = random.randint(10, screen_size[1]) + self.position[1]
            self.xy_list_rain.append((tmp_x, tmp_y))
            self.xy_list_rain.append((tmp_x, tmp_y_2))

    def Draw(self, f):
        f.PolyLineOneColor(self.xy_list, self.color)

    def DrawRain(self, f):
        for i in range(0, len(self.xy_list_rain),2):
            f.Line(self.xy_list_rain[i], self.xy_list_rain[i+1], 0x00BBCC)
