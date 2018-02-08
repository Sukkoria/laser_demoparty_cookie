# -*- coding: utf-8 -*-

from globalVars import *
import frame
import time
import vectors
import random
import numpy
import gstt

CURVE_OFFSET = vectors.Vector2D(screen_size[0]/2,screen_size[1]/2)

class MathCurve(object):
    def __init__(self, degree, symmetry =1):
        # Parse arguments
        self.degree = numpy.max(degree, 0)
        self.symmetry = symmetry
        # Define points
        self.xs = numpy.linspace(0, screen_size[0]/2, num=screen_size[0]/20)
        self.ys = numpy.linspace(0, screen_size[0]/2, num=screen_size[0]/20)
        self.rs = [0 for i in range(len(self.xs))]
        self.angles = [numpy.pi*2*k/self.symmetry for k in range(self.symmetry)]

        random.seed()
        self.c = 0xFF0000
        self.sense_offset = 0
        self.coeff = [(random.random()*2 - 1) for i in range(degree)]
        #print("coeffs", self.coeff)

    def Change(self):
        old_coeffs = self.coeff
        random.seed()
        for i in range(len(self.coeff)):
            self.coeff[i] += (random.random()*2 - 1)
        #print(rand_part)

    def SetSense(self,new_sense):
        self.sense = new_sense
        if(new_sense=="trig"):
            self.sense = "trig"
            self.sense_offset = 1
        elif(new_sense == "antitrig"):
            self.sense = "antitrig"
            self.sense_offset = -1
        else:
            self.sense = "random"
            self.sense_offset = 0

    def UpdateAngles(self):
        for angle in self.angles:
            angle += self.sense_offset

    def Draw(self, f):
        xy_list = []
        for i in range(len(self.xs)):
            tmp_y = 0
            pow_i = 0
            for j in range(self.degree):
                pow_i = numpy.power(self.xs[i],j)
                tmp_y += self.coeff[j]*pow_i
                #xy_list.append((self.xs[i], tmp_y).ToTuple())
                
            #if (tmp_y > screen_size[1]/3):
                #tmp_y = screen_size[1]/3
                #print("too big")
            #elif (tmp_y < -screen_size[1]/3):
                #tmp_y = -screen_size[1]/3
            self.ys[i] = tmp_y
            self.rs[i] = numpy.sqrt(numpy.power(self.xs[i], 2)+ numpy.power(self.ys[i], 2))
        
        for a in range(len(self.angles)):
            #self.angles[a] += self.sense_offset
            #angle += 0.5
            print(self.angles[a])
            for i in range(len(self.rs)):
                xy_list.append((CURVE_OFFSET + vectors.Vector2D(self.rs[i]*numpy.cos(self.angles[a]),self.rs[i]*numpy.sin(self.angles[a]))).ToTuple())
        f.PolyLineOneColor(xy_list, 0x0000FF)

'''
Old version
        if self.symmetry == 1:
            for i in range(len(self.xs)):
            #xy_list.append((CURVE_OFFSET + vectors.Vector2D(self.xs[i]*screen_size[0]/2,self.ys[i])).ToTuple())
                 xy_list.append((CURVE_OFFSET + vectors.Vector2D(self.xs[i],self.ys[i])).ToTuple())
        elif self.symmetry == 2:
            for i in range(len(self.xs)):
                xy_list.append((CURVE_OFFSET + vectors.Vector2D(self.xs[i],self.ys[i])).ToTuple())
            for i in range(len(self.xs)):
                xy_list.append((CURVE_OFFSET + vectors.Vector2D(-self.xs[i],-self.ys[i])).ToTuple())
        ##print(xy_list[0])
        #f.PolyLineOneColor(xy_list, 0xFF00FF)
'''
