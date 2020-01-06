import sys
import pygame
import random
from pygame.math import Vector3
# Initialize pygame so it runs in the background and manages things
pygame.init()

# create colors
light_blue = Vector3(173, 216, 230)
navy = Vector3(2, 7, 93)
white = Vector3(255, 255, 255)
# make it change slowly
color_counter = 0

color_step = .00003
# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1000, 500) )
print(pygame.QUIT)

#images used
sun = pygame.image.load("src/img/Sun_with_sunglasses[1].jpg")
raccoon = pygame.image.load("src/img/raccoon-revised-md[1].png")
r = raccoon.get_rect()
#make a font object
font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render('Catch the Raccoons before daytime!', True, white) 

# x and y of raccoons
x = 300
y = 100
#create timer event
clock = pygame.time.Clock()
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 2000)

def did_catch_raccoon():
    """figure out if raccoon was clicked on"""
    pass

def update_score():
    """display number of raccoons caught"""
    pass
    
# Main loop. Your game would go inside this loop
while True:
    # make screen change color over time
    screen.fill(navy.lerp(light_blue, color_counter))
    # make text appear 
    screen.blit(text, (200,10))
    # make sun pop up
    if color_counter == 1:
        screen.blit(sun, (700,50))
    
    #to change color of background in increments and then stop
    if color_counter < 1:
        color_counter += color_step
        if color_counter > 1:
            color_counter = 1
    


    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        if event.type == TIMEREVENT:
            x = random.randint(0, 1000 - raccoon.get_width())
            y = random.randint(0, 500 - raccoon.get_height())
            r.x = x
            r.y = y

            r = raccoon.get_rect()
        # This line will print each event to the terminal
            print(event)
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
        # If so, exit the program
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if r.collidepoint(pygame.mouse.get_pos()):
                x = random.randint(0, 1000 - raccoon.get_width())
                y = random.randint(0, 500 - raccoon.get_height())
                r.x = x
                r.y = y
                
        
    screen.blit(raccoon,(x,y))
    pygame.display.flip()
    
        



   
