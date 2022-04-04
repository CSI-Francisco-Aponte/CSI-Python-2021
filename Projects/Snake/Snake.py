#the screen of the game is created using pygame, therefore the program needs pygame
import pygame
#This imports time into the code, and all its functions
import time
#This begins the game
pygame.init()

#This creates 3 variables that each are 3 different colors. The numbers are organized in RGB, red green and blue, each numer represents how much of each color is applied. All 0 means black and all 255 means white.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#This establishes the width of the screen
dis_width = 800
#This establishes the height of the screen
dis_height  = 600
#This creates the display or the screen that the game takes place
dis = pygame.display.set_mode((dis_width, dis_width))

# This makes the window that opens, the screen, to have the caption or be named "Snake game by Edureka"
pygame.display.set_caption('Snake game by Edureka')

# First a variable is created called game over and then a loop is created using that variable. The loop is runs while the game is not over. This causes the game not to open and close immedietly as it previously did.
game_over = False

#This establishes the location in terms of the x axis where the snake begins the game
x1 =dis_width/2
#This establishes the location in terms of the y axis where the snake begins the game
y1 =dis_width/2
#This establishes how big the snake block is
snake_block = 10

# Here the variables for how much the x and y values are changed
x1_change = 0       
y1_change = 0
 
#This creates a timer in the game
clock = pygame.time.Clock()

#This creates a variable used in a later function to set the speed of the snake. a variable is created to be able to manipulate the speed of the snake in later codes
snake_speed=30

#This establishes the font for the game
font_style = pygame.font.SysFont(None, 50)
 
#This defines the function called message. Which is relatively self-explanatory, it displays messages on the display
def message(msg,color):
    #This establishes the parameters of msg
    mesg = font_style.render(msg, True, color)
    #This establishes the coordinates in which the message will be
    dis.blit(mesg, [dis_width/2, dis_height/2])


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
 
#Here the program changes the value of the variable game_over to true if the snake touches any of the edges of the display, ending the game
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

# the variables x1 and y1 change as long as the x1_change and y1_change varibles changes too
    x1 += x1_change
    y1 += y1_change
#Here it makes the entire display completely white
    dis.fill(white)
# this draws a rectangle on the display colored black on the corrdinates of x1 and y1 with the dimensions 10x10, which is how big the snake block is
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

#This sets the speed that the snake goes using the variable created earlier
    clock.tick(snake_speed)

#This displays the words You lost on the screen in red when the player loses
message("You lost",red)
#This updates the display
pygame.display.update()
#This tells the program that after the player has lost, to display the you lost on the screen for 2 secons before ending the game
time.sleep(2)

#This ends the game
pygame.quit()
quit()