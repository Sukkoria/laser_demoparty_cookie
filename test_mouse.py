# coding=UTF-8

import pygame

pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            print pygame.mouse.get_pos()
            print pygame.mouse.get_rel()
