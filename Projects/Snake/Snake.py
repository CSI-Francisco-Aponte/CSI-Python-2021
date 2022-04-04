#the screen of the game is created using pygame, therefore the program needs pygame
import pygame

#This begins the game
pygame.init()

#This creates 3 variables that each are 3 different colors. The numbers are organized in RGB, red green and blue, each numer represents how much of each color is applied. All 0 means black and all 255 means white.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#This creates the screen display of the game and sets its dimensions
dis=pygame.display.set_mode((800,600))

# This makes the window that opens, the screen, to have the caption or be named "Snake game by Edureka"
pygame.display.set_caption('Snake game by Edureka')

# First a variable is created called game over and then a loop is created using that variable. The loop is runs while the game is not over. This causes the game not to open and close immedietly as it previously did.
game_over = False

#Here 2 variables are created x1 and y1 which are manipulated later in the code to change the x and y values of the snake
x1 = 300
y1 = 300
 
# Here the variables for how much the x and y values are changed
x1_change = 0       
y1_change = 0
 
#This creates a timer in the game
clock = pygame.time.Clock()
 
#This is the block of code used to control the snake, every time the arrows are pressed, the snake changes x or y by 10 depending on which arrow in which direction is pressed.
while not game_over:
    #This creates a for loop with everything in the list
    for event in pygame.event.get():
    #Here the program notices if the user wants to close the game, it switches the variable game_over to true and closes the program
        if event.type == pygame.QUIT:
            game_over = True
        #This uses the function KEYDOWN to move the snake
        if event.type == pygame.KEYDOWN:
        #Here if the left arrow is pressed, the snake moves -10 spaces in the x axis or 10 spaces to the left
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
        #Here if the right arrow is pressed, the snake moves 10 spaces in the x axis, or 10 spaces to the right.
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
        #Here if the up arrow is pressed, the snake moves -10 spaces in the y axis, or up ten spaces
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
        #Here if the down arrow is pressed, the snake moves 10 spaces in the y axis, or 10 spaces down
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 

# the variables x1 and y1 change as long as the x1_change and y1_change varibles changes too
    x1 += x1_change
    y1 += y1_change
#Here it makes the entire display completely white
    dis.fill(white)
# this draws a rectangle on the display colored black on the corrdinates of x1 and y1 with the dimensions 10x10
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

#This piece of coding updates the screen.
    pygame.display.update()

#This sets the speed that the timer runs.
    clock.tick(30)

#This ends the game
pygame.quit()
quit()