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

#Here 2 variables are created, red and blue, the numbers to its side are formatted using RGP: Red, green, and blue, 255 being the maximun you can have of that color. FOr the blue varible, there is 0 green, 0 red, and max 255 of blue, vice versa for the red. To have a color like purple it would be equal for red and blue and 0 green. 0,0,0 is black, and 255,255,255 is white. 
blue=(0,0,255)
red=(255,0,0)

# First a variable is created called game over and then a loop is created using that variable. The loop is runs while the game is not over. This causes the game not to open and close immedietly as it previously did.
game_over=False
while not game_over:
    for event in pygame.event.get():
        #This makes so when the close button on the screen is pressed, the screen quits or closes
        if event.type==pygame.QUIT:
            game_over=True
#Here the the snake is drawn. To draw the snake the function draw.rect() is used, then the variable made before makes the rectangle blue and after that the numbers represent
    pygame.draw.rect(dis,blue,[200,150,10,10])
    pygame.display.update()

#This ends the game
pygame.quit()
quit()