# coding=UTF-8
'''
Unnamed Laser project
Based on Empty Laser by Sam Neurohack (CC)

Lazer Game Jam 2017 (8.04 and 9.04)

Code by CMB and Miaou
'''


# REQUIRED
import pygame # https://www.pygame.org/docs/
#import pylibmc

# STANDARD LIBS
import math
import random
import itertools
import sys
import os
import thread
import time
import numpy

# OTHER FILES OF THE PROJECT
import gstt # Global game object
import renderer # Two renderers : laser and on screen
import dac # Communicate with the etherdrean/laser
import frame # Buffer for the points and beams
from globalVars import * # Global variables (aka configuration)
from vectors import Vector2D # To manipulate the points

# MODULES
import logo # Simple logo
import harp # Interactive laser harp, can be used as moving laser ceiling
import mathcurve
import koch
import smiley
import abstractrandom as absrand
#import menu
# Imports for Pong 
import ball, score, score2, borders, filet, flips, text, title
# Further modules (games, …) are to be included here

import grid
'''
Launch a thread to communicate with the Etherdream (and the laser)
(Don’t touch, it works !)
'''
def dac_thread(): 
	while True:
		try:

			d = dac.DAC(dac.find_first_dac())
			d.play_stream(laser)

		except Exception as e:
		        print e
                        if OFFLINE: #and e=="[Errno 101] Network is unreachable\n":To refine for
                            #other errors
                            #print "netwrok"
                            pass
                        else:
			    import sys, traceback
			    print '\n---------------------'
                            print 'Exception: %s' % e
			    print '- - - - - - - - - - -'
			    traceback.print_tb(sys.exc_info()[2])
			    print "\n"
			    pass

'''
Displays a calibration pattern with all the colors, to check their balance 
'''
def DrawCalPattern(f): # When C is pressed
    l, h = screen_size

    # Recreate the famous "TOP"
    f.Line((0, 0), (l, 0), 0xFFFFFF)
    f.LineTo((l, h), 0xFFFFFF)
    f.LineTo((0, h), 0xFFFFFF)
    f.LineTo((0, 0), 0xFFFFFF)
    f.LineTo((l, h), 0xFFFFFF)
    f.LineTo((l/2, h), 0xFFFFFF)
    f.LineTo((l/2, 0), 0xFFFFFF)
    f.LineTo((l, 0), 0xFFFFFF)
    f.LineTo((0, h), 0xFFFFFF)
    f.LineTo((0, h/2), 0xFFFFFF)
    f.LineTo((l, h/2), 0xFFFFFF)

    letters = [
            #T
            [[(10,h/3), (l/6, h/3)],0xFF0000],
            [[(l/6,h/3), (l/6, 2*h/3)],0xFF0000],
            [[(l/6,2*h/3), (l/6, h/3)],0xFF0000],
            [[(l/6,h/3), (l/3-10, h/3)],0xFF0000],
            # O
            [[(l/3 +10, h/3), (2*l/3-10, h/3)], 0x00FF00],
            [[(2*l/3 -10, h/3), (2*l/3-10, 2*h/3)], 0x00FF00],
            [[(2*l/3 -10, 2*h/3), (l/3+10, 2*h/3)], 0x00FF00],
            [[(l/3 +10, 2*h/3), (l/3+10, h/3)], 0x00FF00],
            # P
            [[(2*l/3 + 10, 2*h/3), (2*l/3 + 10, h/3)], 0x0000FF],
            [[(2*l/3 + 10, h/3), (l- 10, h/3)], 0x0000FF],
            [[(l- 10, h/3), (l- 10, 1.5*h/3)], 0x0000FF],
            [[(l- 10, 1.5*h/3), (2*l/3+ 10, 1.5*h/3)], 0x0000FF],
            ]
    for points in letters:
        col = points[1]
        xy_list = []
        for coord in points[0]:
            xy_list.append((Vector2D(coord[0], coord[1])).ToTuple())
        f.PolyLineOneColor(xy_list,col)
    
'''
Align the renderer on the projection zone
Used when zooming/scaling/rotating the zone
'''
def Align(f): 
	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)

	print str(gstt.centerx) + "," + str(gstt.centery) + "," + str(gstt.zoomx) + "," + str(gstt.zoomy) + "," + str(gstt.sizex) + "," + str(gstt.sizey)

# Let the show begin !
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Unnamed project")
clock = pygame.time.Clock()

# Get variables (from globalvariables.py)
gstt.centerx = LASER_CENTER_X
gstt.centery = LASER_CENTER_Y
gstt.zoomx = LASER_ZOOM_X
gstt.zoomy = LASER_ZOOM_Y
gstt.sizex = LASER_SIZE_X
gstt.sizey = LASER_SIZE_Y
gstt.finangle = LASER_ANGLE

gstt.buffer = ""

fwork_holder = frame.FrameHolder()
laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)

thread.start_new_thread(dac_thread, ())
keystates = pygame.key.get_pressed()
update_screen = False

keep_lasing = True
gstt.fs = GAME_FS_MENU
gstt.initiating = False

gstt.send_enter = False

# Rendering loop
while keep_lasing:
	# Create a new frame
	l,h = screen_size
	fwork = frame.Frame()
        # Manage events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gstt.fs = GAME_FS_QUIT	
        last_keystates = keystates[:] # Save the previous keystates to avoid false detections
	keystates = pygame.key.get_pressed()[:] # Array of 105 values (for each key of the keyboard) 
        keymods = pygame.key.get_mods()
        print keymods
        # Modifiers : to be used with CTRL pressed (to avoid conflicts with the different modes)
        # TO DO : Find a way to "block" edition (password ?)
        if keymods == 64 or keymods == 128: # Left or right key
            # RTYU to set the zone	
            if keystates[pygame.K_r]:
	        gstt.centerx += 20
		Align(fwork)

	    if keystates[pygame.K_t]:
	        gstt.centerx -= 20
		Align(fwork)
		
            if keystates[pygame.K_y]:
	        gstt.centery += 20
		Align(fwork)

	    if keystates[pygame.K_u]:
		gstt.centery -= 20
		Align(fwork)
            # FGHJ for the zooms
	    if keystates[pygame.K_f]:
		gstt.zoomx += 0.1
		Align(fwork)

            if keystates[pygame.K_g]:
		gstt.zoomx -= 0.1
		Align(fwork)
		
	    if keystates[pygame.K_h]:
		gstt.zoomy += 0.1
		Align(fwork)

	    if keystates[pygame.K_j]:
		gstt.zoomy -= 0.1
		Align(fwork)
	    # CVBN for the size along X and Y
	    if keystates[pygame.K_c]:
		gstt.sizex -= 50
		Align(fwork)
		
	    if keystates[pygame.K_v]:
		gstt.sizex += 50
		Align(fwork)
		
	    if keystates[pygame.K_b]:
		gstt.sizey -= 50
		Align(fwork)
		
	    if keystates[pygame.K_n]:
		gstt.sizey += 50
		Align(fwork)
		
	    if keystates[pygame.K_l]:
		gstt.finangle -= 0.001
		Align(fwork)
		
	    if keystates[pygame.K_m]:
		gstt.finangle += 0.001
		Align(fwork)
	    # Ctrl+A to send enter (for text option)
            if keystates[pygame.K_a]:
                gstt.send_enter = True
                #print("enter")
                
	# "Nude" keys to select menu options
        else:
            # ESC : exit
	    keep_lasing=not keystates[pygame.K_ESCAPE] 
            # C : switch to calibration figure
            if keystates[pygame.K_c] and not last_keystates[pygame.K_c]:
                if gstt.fs == GAME_FS_MENU:
                    gstt.fs = GAME_FS_CAL
                else:
                    gstt.fs = GAME_FS_MENU
            # H : launch Laser Harp
            if keystates[pygame.K_h] and not last_keystates[pygame.K_h]:
                if gstt.fs == GAME_FS_MENU:
                    gstt.fs = GAME_FS_HARP
                    gstt.initiating = True
                elif gstt.fs == GAME_FS_HARP:
                    gstt.fs = GAME_FS_MENU
            # R : launch Abstract Random
            if keystates[pygame.K_r] and not last_keystates[pygame.K_r]:
                if gstt.fs == GAME_FS_MENU:
                    gstt.fs = GAME_FS_ABSRAND
                    gstt.initiating = True
                elif gstt.fs == GAME_FS_ABSRAND:
                    gstt.fs = GAME_FS_MENU
            # P : launch Pong
            if keystates[pygame.K_p] and not last_keystates[pygame.K_p]:
                if gstt.fs == GAME_FS_MENU:
                    gstt.fs = GAME_FS_PLAY_PONG
                    gstt.initiating = True
                elif gstt.fs == GAME_FS_PLAY_PONG:
                    gstt.fs = GAME_FS_MENU
            # T : launch Text mode    
            if keystates[pygame.K_t] and not last_keystates[pygame.K_t]:
                if gstt.fs == GAME_FS_MENU:
                    gstt.fs = GAME_FS_TEXT
                    gstt.initiating = True
                elif gstt.fs == GAME_FS_TEXT:
                    gstt.fs = GAME_FS_MENU
            # M : launch MathCurve mode
            if keystates[pygame.K_m] and not last_keystates[pygame.K_m]:
                if gstt.fs == GAME_FS_MENU:
                    gstt.fs = GAME_FS_MATH_CURVE
                    gstt.initiating = True
                elif gstt.fs == GAME_FS_MATH_CURVE:
                    gstt.fs = GAME_FS_MENU
            # K : launch Koch mode
            if keystates[pygame.K_k] and not last_keystates[pygame.K_k]:
                if gstt.fs == GAME_FS_MENU:
                    gstt.fs = GAME_FS_KOCH
                    gstt.initiating = True
                elif gstt.fs == GAME_FS_KOCH:
                    gstt.fs = GAME_FS_MENU
            # O : launch Morph mode
            if keystates[pygame.K_o] and not last_keystates[pygame.K_o]:
                if gstt.fs == GAME_FS_MENU:
                    gstt.fs = GAME_FS_MORPH
                    gstt.initiating = True
                elif gstt.fs == GAME_FS_MORPH:
                    gstt.fs = GAME_FS_MENU

            
        # Erase previous rendered frame
	screen.fill(0)

	''' Example of a white square (Corentin)
	fwork.Line((0, 0), (l, 0), 0xFFFFFF)
	fwork.LineTo((l, h), 0xFFFFFF)
	fwork.LineTo((0, h), 0xFFFFFF)
	fwork.LineTo((0, 0), 0xFFFFFF)
	'''
	laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)
	gstt.zoomx-=0.01
	gstt.zoomy-=0.01

	#print update_screen



        # Compute actions/modes
        if gstt.fs == GAME_FS_MENU:
            logo.Draw(fwork)
        elif gstt.fs == GAME_FS_CAL:
            DrawCalPattern(fwork)
        # HARP
        elif gstt.fs == GAME_FS_HARP:
            if gstt.initiating:
                gstt.hrp = harp.Harp()  
                gstt.initiating = False
                gstt.hrp.current_string = 0
            random.seed()
            for i in range(strings):
                gstt.hrp.Color(i, i)
	    up_key = keystates[pygame.K_UP]
	    down_key = keystates[pygame.K_DOWN] 
	    left_key = keystates[pygame.K_LEFT] and not last_keystates[pygame.K_LEFT]
	    right_key = keystates[pygame.K_RIGHT] and not last_keystates[pygame.K_RIGHT]
            
            if left_key and not gstt.hrp.current_string ==0:
                gstt.hrp.current_string -= 1
            if right_key and not gstt.hrp.current_string == strings:
                gstt.hrp.current_string += 1
            if down_key:
                gstt.hrp.offset[gstt.hrp.current_string] += 10
            if up_key:
                gstt.hrp.offset[gstt.hrp.current_string] -= 10


            gstt.hrp.Draw(fwork)

        # ABSRAND
        elif gstt.fs == GAME_FS_ABSRAND:
            if gstt.initiating:
                gstt.absrand = absrand.Absrand()
	    up_key = keystates[pygame.K_UP]
	    down_key = keystates[pygame.K_DOWN]
	    left_key = keystates[pygame.K_LEFT]
	    right_key = keystates[pygame.K_RIGHT]
	    gstt.absrand.Move(up_key, down_key, left_key, right_key)
            if keystates[pygame.K_l] or random.randint(0,3)==0:
                gstt.absrand.Launch(fwork)
            #if keystates[pygame.K_m] or random.randint(0,2)==0:
                #gstt.absrand.
            gstt.absrand.Draw(fwork)
        # PONG
        elif gstt.fs == GAME_FS_PLAY_PONG:
            if gstt.initiating:
                gstt.score = score.Score()
                gstt.score2 = score2.Score2()
                gstt.bll = ball.Ball()
                gstt.flp = flips.Flips()
                gstt.txt = text.Text()
                gstt.flt = filet.Filet()
                gstt.brdrs = borders.Borders()
                gstt.xvel = -1
                gstt.yvel = 0
                gstt.lscore = 0
                gstt.rscore = 0
                gstt.ly = FLIPS_lorigin[1]
                gstt.ry = FLIPS_rorigin[1]
                flipsy = [gstt.ly, gstt.ry]
                gstt.stick = 0
                gstt.x = ball_origin[0]
                gstt.y = ball_origin[1]
            #gstt.
        # TEXT
        elif gstt.fs == GAME_FS_TEXT:
            if gstt.initiating:
                gstt.tmessage = "LASER"
                gstt.ttl = title.Text()
                gstt.initiating = False
            if not gstt.send_enter:
                #if (pygame.key.name())
                if event.type == pygame.KEYDOWN:

                    gstt.buffer += pygame.key.name(event.key)
                print gstt.buffer
                #print gstt.buffer
            else:
                gstt.tmessage = gstt.buffer
                gstt.buffer = ""
            #print keymods 
            gstt.ttl.Draw(fwork)
        # MATH CURVE 
        elif gstt.fs == GAME_FS_MATH_CURVE:
            if gstt.initiating:
                gstt.mc = mathcurve.MathCurve(3, 6) # Give the degree of the polynom
                gstt.initiating = False
            gstt.mc.SetSense("trig")
            gstt.mc.UpdateAngles()
            gstt.mc.Change()
            gstt.mc.Draw(fwork)
        # KOCH
        elif gstt.fs == GAME_FS_KOCH:
            if gstt.initiating:
                gstt.kh = grid.Grid(screen_size[1]/2)
                #gstt.kh = smiley.Smiley("devil")
                gstt.initiating = False
                print ("init Koch")
            gstt.kh.Compute()
            #gstt.kh.Rotate(0.1)
            gstt.kh.Draw(fwork)
        # MORPH
        # TO DO



        # Render frame
	fwork_holder.f = fwork
	fwork.RenderScreen(screen)
	pygame.display.flip() # Necessary to avoid blinking
	'''
	if update_screen:
		update_screen = False
		fwork.RenderScreen(screen)
		pygame.display.flip()
	else:
		update_screen = True
	'''
	
	# TODO : rendre indépendante la fréquence de rafraîchissement de l'écran par
	# rapport à celle de l'animation du jeu
	clock.tick(100)


pygame.quit()
