# -*- coding: utf-8 -*-

from globalVars import *
import frame
import time
import vectors
import random
import numpy
import gstt

KOCH_OFFSET = vectors.Vector2D(0,screen_size[1]/2)

class Koch(object):
    def __init__(self, steps):
        self.xs = [0, screen_size[0]/2, screen_size[0]]
        self.ys = [0, 0, 0]

        self.steps = steps
        self.current_step = 0 # init

    def process(self, i1, i2):
        vect = vectors.Vector2D(self.xs[i2]-self.xs[i1], self.ys[i2]- self.ys[i1])
        dist = numpy.sqrt(numpy.power(vect.ToTuple()[0],2)+numpy.power(vect.ToTuple()[1], 2))
        self.new_xs.append(i1)
        self.new_xs.append(i1)
        self.new_xs.append(i1)
        self.new_ys.append(i2)
        self.new_ys.append(i2)
        self.new_ys.append(i2)
        print (dist, len(self.new_xs), len(self.new_ys))

    def Draw(self, f):
        xy_list = []
        # Processing loop
        #print (self.current_step, self.steps)
        if (self.current_step<=self.steps):
            print (self.current_step)
            #self.old_xs = self.xs
            #self.old_ys = self.ys
            #self.xs = []
            #self.ys = []

            self.new_xs = []
            self.new_ys = []
            for i in range(len(self.xs)-1):
                self.process(i, i+1)
                print("in loop", i, i+1)
                #print (len(self.xs), len(self.ys))
                #print (len(self.old_xs), len(self.old_ys))

            self.current_step += 1
            self.xs = self.new_xs
            self.ys = self.new_ys
        else:
            self.current_step = 0
            self.xs = [0, screen_size[0]/2, screen_size[0]]
            self.ys = [0, 0, 0]


        # Drawing loop
        for i in range(len(self.xs)):
            xy_list.append((KOCH_OFFSET + vectors.Vector2D(self.xs[i], self.ys[i])).ToTuple())
            print("xy", xy_list[i])
        f.PolyLineOneColor(xy_list, 0xFF0000)

        
