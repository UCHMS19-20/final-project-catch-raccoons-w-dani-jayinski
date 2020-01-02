import sys
import pygame
from pygame.math import Vector3

# Initialize pygame so it runs in the background and manages things
pygame.init()

# create colors
light_blue = Vector3(173, 216, 230)
navy = Vector3(2, 7, 93)
white = Vector3(255, 255, 255)
# make it change slowly
color_counter = 0
# color_step = 0.00003
color_step = .0001
# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (800, 600) )
print(pygame.QUIT)

#images used
sun = pygame.image.load("src/img/Sun_with_sunglasses[1].jpg")
raccoon = pygame.image.load("src/img/cute-grey-raccoon-free-clip-art-830x497[1].png")

#make a font object
font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render('Catch the Raccoons before daytime!', True, white) 

# Main loop. Your game would go inside this loop
while True:
    #to change color of background in increments and then stop
    if color_counter < 1:
        color_counter += color_step
        if color_counter > 1:
            color_counter = 1
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():

        # This line will print each event to the terminal
        print(event)

        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    # make screen change color over time
    screen.fill(navy.lerp(light_blue, color_counter))
    # make text appear 
    screen.blit(text, (100,10))
    # make sun pop up
    if color_counter == 1:
        screen.blit(sun, (500,50))
    
    pygame.display.flip()
    
        



    #make text of game pop up
