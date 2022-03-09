#the screen of the game is created using pygame, therefore the program needs pygame
import pygame

#This begins the game
pygame.init()

#This creates the screen display of the game and sets its dimensions
dis=pygame.display.set_mode((400,300))

#Thiis is used to make any changes to the screen
pygame.display.update()

# This makes the window that opens, the screen, to have the caption or be named "Snake game by Edureka"
pygame.display.set_caption('Snake game by Edureka')

# First a variable is created called game over and then a loop is created using that variable. The loop is runs while the game is not over. This causes the game not to open and close immedietly as it previously did.
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)

#This ends the game
pygame.quit()
quit()