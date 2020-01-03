import sys
import pygame
import random

# Initialize pygame so it runs in the background and manages things
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()

# create colors
light_blue = pygame.Color(173, 216, 230)
navy = pygame.Color(2, 7, 93)
white = pygame.Color(255, 255, 255)
# make it change slowly
color_counter = 0
# color_step = 0.00003
color_step = .0005
# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1000, 500) )
print(pygame.QUIT)

#images used
sun = pygame.image.load("src/img/Sun_with_sunglasses[1].jpg")
raccoon = pygame.image.load("src/img/raccoon-revised-md[1].png")

#make a font object for title/instructions
font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render('Catch the raccoons before daytime!', True, white) 


 # to make raccoons pop up at locations
class Raccoon_popup:
    def __init__(self):
        #width of raccoon
        self.RACCOON_WIDTH = 90
        self.RACCOON_HEIGHT = 81
        #set score starting at zero 
        self.score = 0
        # Font object for displaying score text
        self.FONT_SIZE = 31
        self.font_obj = pygame.font.Font('./fonts/GROBOLD.ttf', self.FONT_SIZE)
        #make raccoons pop up
        self.raccoons = []
        self.raccoons.append(raccoon.subsurface(169, 0, 90, 81))
        self.raccoons.append(raccoon.subsurface(309, 0, 90, 81))
        self.raccoons.append(raccoon.subsurface(449, 0, 90, 81))
        self.raccoons.append(raccoon.subsurface(575, 0, 116, 81))
        self.raccoons.append(raccoon.subsurface(717, 0, 116, 81))
        self.raccoons.append(raccoon.subsurface(853, 0, 116, 81))
         # Positions of the holes in background
        self.hole_positions = []
        self.hole_positions.append((381, 295))
        self.hole_positions.append((119, 366))
        self.hole_positions.append((179, 169))
        self.hole_positions.append((404, 479))
        self.hole_positions.append((636, 366))
        self.hole_positions.append((658, 232))
        self.hole_positions.append((464, 119))
        self.hole_positions.append((95, 43))
        self.hole_positions.append((603, 11))
    # Check whether the mouse click caught the raccoon or not
    def is_raccoon_caught(self, mouse_position, current_hole_position):
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        current_hole_x = current_hole_position[0]
        current_hole_y = current_hole_position[1]
        if (mouse_x > current_hole_x) and (mouse_x < current_hole_x + self.RACCOON_WIDTH) and (mouse_y > current_hole_y) and (mouse_y < current_hole_y + self.RACCOON_HEIGHT):
            return True
        else:
            return False
    #update score
    def update_score(self):
        current_score_string = "SCORE: " + str(self.score)
        score_text = self.font_obj.render(current_score_string, True, (255, 255, 255))
        screen.blit(score_text, (10,500))


    for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == self.LEFT_MOUSE_BUTTON:
                    
                if self.is_raccoon_caught(mouse.get_pos(), self.hole_positions[frame_num]) and num > 0 and left == 0:
                        num = 3
                        left = 14
                        is_down = False
                        interval = 0
                        self.score += 1  # Increase player's score
   
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
    
  
   
   
#WHAT I NEED TO DO:
# figure out how to fix the raccoons popping up,
# figure out if a raccooon is clicked

# keep track of and display how many were clicked on
        # This line will print each event to the terminal
            print(event)

        # Check to see if the current event is a QUIT event
            if event.type == pygame.QUIT:
            # If so, exit the program
                sys.exit()
  
    pygame.display.flip()
    
        



   
