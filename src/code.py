import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# create colors
light_blue = pygame.Color(173, 216, 230)
navy = pygame.Color(2, 7, 93)

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 350) )
print(pygame.QUIT)

#make screen change color over time


# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():

        # This line will print each event to the terminal
        print(event)

        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()