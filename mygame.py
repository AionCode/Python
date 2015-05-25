#!/usr/bin/python

import sys, pygame,pygame.mixer
pygame.init()

size =width, height = 600,400
black = 0,0,0

screen = pygame.display.set_mode(size)

tux = pygame.image.load("tux.png")

x = 0
y = 0
r = 0
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:sys.exit()

	screen.fill((r,0,0))
	screen.blit(tux,(200,200))
 	screen.blit(tux,(x,y))  

	pygame.display.flip()
	x = x+1
	y = y+1
	if r == 255:
		r1 = -1
	elif r == 0:
		r1 = 1
	r = r+r1
