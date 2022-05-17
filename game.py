# Imports
from oslaAgent import oslaAgent
from rlAgent import RLAgent
from sequence import Sequence
from board import Board 
from position import Position 
from simulator import Simulator
from leftMostAgent import LeftMostAgent
from rightMostAgent import RightMostAgent
from randomAgent import RandomAgent
import pygame




# --------------------------- PRE GAME SETUPS --------------------------------------------
pygame.init()

# Set up the drawing window and game board
screen = pygame.display.set_mode([500, 500])

# Set up text font and instances
base_font = pygame.font.Font(None, 32)

# Input interface
p1_text = ''
p2_text = ''
play_button_text = "PLAY"

# Set up visual interface boxes
play_button_rect = pygame.Rect(220, 33.5, 60, 25)
input_rect_p1 = pygame.Rect(40, 25, 40, 40)
input_rect_p2 = pygame.Rect(420, 25, 40, 40)

# Set up interface colors 
color = pygame.Color('lightgray')
play_button_color = (50, 200, 50)

# The game starts in the first player's turn 
p1_turn = True
validPlays = ["1", "2", "3", "4", "5", "6", "7"]

# Agents initialization 
a1 = LeftMostAgent()
a2 = RightMostAgent()
aRandom = RandomAgent()
aOsla = oslaAgent(2)
aRl = RLAgent("RLAgent1v2",1)

#decide the players here
p1 = aRl
p2 = aOsla

# Game board and simulator for agents to run automatically 
gb = Board()
sim = Simulator(p1, p2, 6000, gb, "statsfile1v2.csv")




# ---------------------------- GAME CYCLE -----------------------------------------------
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Play button, input confirmation when playing without simulator 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                if p1_turn:
                    if(p1_text not in validPlays):
                        print("Invalid move, try again, the input should be a single number [1,7]")
                    else:
                        gb.placePiece(int(p1_text)-1,1)
                        p1_text = ""
                        p1_turn = False
                else:
                    if(p2_text not in validPlays):
                        print(p2_text)
                        print("Invalid move, try again, the input should be a single number [1,7]")
                    else:
                        gb.placePiece(int(p2_text)-1,2)
                        p1_turn = True
                        p2_text = ""
                        
                if gb.checkWinner():
                    gb.reset()
                    p1_turn = True
  
        # Input Event Handling when playing without simulator 
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                if p1_turn:
                    p1_text = p1_text[:-1]
                else:
                    p2_text = p2_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                if p1_turn:
                    p1_text += event.unicode
                else:
                    p2_text += event.unicode 

    # Show the game board
    screen.fill((50, 50, 255))
    gb.show(screen)

    # Run Simulator 
    running = sim.run(screen)

    # Visual Interface
    pygame.draw.rect(screen, color, input_rect_p1)
    pygame.draw.rect(screen, color, input_rect_p2)
    pygame.draw.rect(screen, play_button_color, play_button_rect)

    text_surface_p1 = base_font.render(p1_text, True, (0, 0, 0))
    text_surface_p2 = base_font.render(p2_text, True, (0, 0, 0))
    text_surface_play_button = base_font.render(play_button_text, True, (0, 0, 0))

    screen.blit(text_surface_play_button, (play_button_rect.x+1.5, play_button_rect.y+3))

    if p1_turn:
       screen.blit(text_surface_p1, (input_rect_p1.x+13, input_rect_p1.y+10))
    else:
        screen.blit(text_surface_p2, (input_rect_p2.x+13, input_rect_p2.y+5))

    # Flip the display
    pygame.display.flip()

pygame.quit()