# Impors
from sequence import Sequence
from board import Board 
from position import Position 
import pygame

pygame.init()

# Set up the drawing window and game board
screen = pygame.display.set_mode([500, 500])
gb = Board()

# Set up text font and instances
base_font = pygame.font.Font(None, 32)

p1_text = ''
p2_text = ''
play_button_text = "PLAY"

# Set up visual interface 
play_button_rect = pygame.Rect(220, 33.5, 60, 25)
input_rect_p1 = pygame.Rect(40, 25, 40, 40)
input_rect_p2 = pygame.Rect(420, 25, 40, 40)

color = pygame.Color('lightgray')
play_button_color = (50, 200, 50)

p1_turn = True
validPlays = ["1", "2", "3", "4", "5", "6", "7"]

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                if p1_turn:
                    if(p1_text not in validPlays):
                        print("Invalid play, try again, the input should be a single number [1,7]")
                    else:
                        gb.placePiece(int(p1_text)-1,1)
                        p1_text = ""
                        p1_turn = False
                else:
                    if(p1_text not in validPlays):
                        print("Invalid play, try again, the input should be a single number [1,7]")
                    else:
                        gb.placePiece(int(p2_text)-1,2)
                        p1_turn = True
                        p2_text = "" 
                gb.gameState()
                if gb.checkWinner():
                    p1_turn = True
  
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