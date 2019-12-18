import sys
import pygame
from pygame.math import Vector3

# Initialize pygame so it runs in the background and manages things
pygame.init()

# create colors
light_blue = Vector3(173, 216, 230)
navy = Vector3(2, 7, 93)
# make it change slowly
color_counter = 0
color_step = 0.00002
# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (800, 600) )
print(pygame.QUIT)



# Main loop. Your game would go inside this loop
while True:
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
    pygame.display.flip()