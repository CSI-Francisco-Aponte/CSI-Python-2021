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
game_over=False

#Here 2 variables are created x1 and y1 which are manipulated later in the code to change the x and y values of the snake
x1 = 300
y1 = 300
 
# Here the variables for how much the x and y values are changed
x1_change = 0       
y1_change = 0
 
#This creates a timer in the game
clock = pygame.time.Clock()
 
#This is the code used to control the snake, every time the arrows are pressed, the snake changes x or y by 10 depending on which arrow in which direction is pressed.
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 

# the variables x1 and y1 change as long as the x1_change and y1_change varibles changes too
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
# this draws a rectangle on the display colored black on the corrdinates of x1 and y1 with the dimensions 10x10
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

#This makes so when the close button on the screen is pressed, the screen quits or close
while not game_over:
    for event in pygame.event.get():s
        if event.type==pygame.QUIT:
            game_over=True
#Here the the snake is drawn. To draw the snake the function draw.rect() is used, then the variable made before makes the rectangle blue and after that the numbers represent the dimension adn the coordinates of the rectangle drawn. The first two is the coordinates, the last two are the dimensions.
    pygame.draw.rect(dis,blue,[200,150,10,10])
#This piece of coding updates the screen.
    pygame.display.update()

#This sets the speed that the timer runs.
clock.tick(30)

#This ends the game
pygame.quit()
quit()