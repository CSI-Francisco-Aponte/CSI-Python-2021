#the screen of the game is created using pygame, therefore the program needs pygame
import pygame
#This imports time into the code, and all its functions
import time
#This imports random into the code, and all its functions
import random
#This begins the game
pygame.init()

#This creates 5 variables that each are 5 different colors. The numbers are organized in RGB, red green and blue, each number represents how much of each color is applied. All 0 means black and all 255 means white.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#This establishes the width of the screen
dis_width = 800
#This establishes the height of the screen
dis_height  = 600
#This creates the display or the screen that the game takes place
dis = pygame.display.set_mode((dis_width, dis_width))

# This makes the window that opens, the screen, to have the caption or be named "Snake game by Edureka"
pygame.display.set_caption('Snake game by Edureka')

#This creates a timer in the game
clock = pygame.time.Clock()

#This establishes how big the snake block is
snake_block = 10
#This creates a variable used in a later function to set the speed of the snake. a variable is created to be able to manipulate the speed of the snake in later codes
snake_speed=30
 
#This establishes the font for the game
font_style = pygame.font.SysFont(None, 50)

#This defines the function called message. Which is relatively self-explanatory, it displays messages on the display
def message(msg,color):
    #This establishes the parameters of msg
    mesg = font_style.render(msg, True, color)
    #This establishes the coordinates in which the message will be
    dis.blit(mesg, [dis_width/3, dis_height/3])
 
#This defines the function gameLoop which creates a boolean variable with the value of false. This means the game is not over
def gameLoop():
    game_over = False
    game_close = False

    #This establishes the location in terms of the x axis where the snake begins the game
    x1 =dis_width/2
    #This establishes the location in terms of the y axis where the snake begins the game
    y1 =dis_width/2

    # Here are the values of x and y of the snake which change depending on how they are manipulated later on
    x1_change = 0       
    y1_change = 0
 
    #This displays a food on the screen on a random x and y coodinate and sets the dimensions of the food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
 
    #This creates a loop that doesnt close the display until the game is over (game_over= True)
    while not game_over:

        #This establishes what happens when the user looses. First it makes the variable game_close True
        while game_close == True:
            #This makes the entire display fill to the color white.
            dis.fill(white)
            #This displays a message on the screen in red
            message("You Lost! Press Q-Quit or C-Play Again", red)
            #This updates the display
            pygame.display.update()
 
            #This for loop is created and establishes that when q is pressed, the game will close. WHen C is pressed, the game will restart.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                #This ends the for loop
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    #This restarts the game
                    if event.key == pygame.K_c:
                        gameLoop()


        #This is the block of code used to control the snake, every time the arrows are pressed, the snake changes x or y by 10 depending on which arrow in which direction is pressed.
        #This creates a for loop with everything in the list
        for event in pygame.event.get():
            #Here the program notices if the user wants to close the game, it switches the variable game_over to true and closes the program
            if event.type == pygame.QUIT:
                game_over = True
            #This uses the function KEYDOWN to move the snake
            if event.type == pygame.KEYDOWN:
                #Here if the left arrow is pressed, the snake moves -10 spaces in the x axis or 10 spaces to the left, becuase the value of snake_block is 10 and since it is negative, then -10
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                #Here if the right arrow is pressed, the snake moves 10 spaces in the x axis, or 10 spaces to the right, becuase the value of snake_block is 10
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                #Here if the up arrow is pressed, the snake moves -10 spaces in the y axis, or up ten spaces, becuase the value of snake_block is 10 and since its negative, then -10
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                #Here if the down arrow is pressed, the snake moves 10 spaces in the y axis, or 10 spaces down, becuase the value of snake_block is 10
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        #Here the program changes the value of the variable game_over to true if the snake touches any of the edges of the display, ending the game
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        #The variables x1 and y1 change as long as the x1_change and y1_change varibles changes too
        x1 += x1_change
        y1 += y1_change
        #Here it makes the entire display completely white
        dis.fill(white)
        #This draws the food in a rectangle, in blue, with the same dimensions as snake_block
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        #This draws the snake in the coordinates that were manipulated before in the dimensions of snake_block
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        #This updates the display
        pygame.display.update()
 
        #This says that when the coordinates of the snake are equal to the coordinates of the food, to print yummy!! on the screen
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
    
        #This sets the speed that the snake goes using the variable created earlier
        clock.tick(snake_speed)


    #This ends the game
    pygame.quit()
    quit()

#This is used for the game to restart. If the user presses c when they lose, it retarts the program.
gameLoop()