import pygame
import random

from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, QUIT

pygame.init()

winner = ""
board = [" "," "," "," "," "," "," "," "," "," "]



turn = "X"
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 20)
font1 = pygame.font.SysFont('Comic Sans MS', 50)



size = width, height = 450, 600
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))

pygame.draw.line(screen, (0, 0, 0), (150, 0), (150, 450))
pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 450))
pygame.draw.line(screen, (0, 0, 0), (0, 150), (450, 150))
pygame.draw.line(screen, (0, 0, 0), (0, 300), (450, 300))


# the square class which will mainly be used to tell if a space is taken or not
# probably a bunch of useless parameters and could have just made rectangle objects
# I'll come back in the future to see
class square:
    def __init__(self, left, top, w = 140, h = 140, color = (255, 255, 255), open = True):
        self.left = left
        self.top = top
        self.open = True
        self.w = w
        self.h = h
        self.color = color
        self.open = open

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.left, self.top, self.w, self.h))

    def take(self):
        self.open = False

    

 

# the board is going to be set up in 9 different squares
# the game will check whose turn it is and what square is clicked
# if the square is available either an x or o will be drawn
# if any of the winning conditions are met or if a draw is met the game ends

sq1 = square(10, 10)
sq1.draw()
sq2 = square(160, 10)
sq2.draw()
sq3 = square(310, 10)
sq3.draw()
sq4 = square(10, 160)
sq4.draw()
sq5 = square(160, 160)
sq5.draw()
sq6 = square(310, 160)
sq6.draw()
sq7 = square(10, 310)
sq7.draw()
sq8 = square(160, 310)
sq8.draw()
sq9 = square(310, 310)
sq9.draw()

squarenum = 0
clicking = False

# main game loop
playing = True
while playing:

    # updates the board variables every turn
    b1 = board[0]
    b2 = board[1]
    b3 = board[2]
    b4 = board[3]
    b5 = board[4]
    b6 = board[5]
    b7 = board[6]
    b8 = board[7]
    b9 = board[8]   

    # fills the bottom of the screen to update and adds new text over to tell whose turn it is
    screen.fill((0, 0, 0), pygame.Rect(0, 450, 450, 150))
    text = font.render(f"{turn}'s turn", True , (255, 255, 255))
    screen.blit(text, (175, 470))

    # if the game is over display the gameover screen WIP
    
    # gets the mouse position every iteration
    mosx, mosy = pygame.mouse.get_pos()
    




    # this will check if the mouse is on any of the squares
    if 0 < mosx < 150 and 0 < mosy < 150:
        squarenum = 1
    elif 150 < mosx < 300 and 0 < mosy < 150:
        squarenum = 2
    elif 300 < mosx < 450 and 0 < mosy < 150:
        squarenum = 3
    elif 0 < mosx < 150 and 150 < mosy < 300:
        squarenum = 4
    elif 150 < mosx < 300 and 150 < mosy < 300:
        squarenum = 5
    elif 300 < mosx < 450 and 150 < mosy < 300:
        squarenum = 6
    elif 0 < mosx < 150 and 300 < mosy < 450:
        squarenum = 7
    elif 150 < mosx < 300 and 300 < mosy < 450:
        squarenum = 8
    elif 300 < mosx < 450 and 300 < mosy < 450:
        squarenum = 9
    else:
        squarenum = 0
    
    
    # checks for events (mouseclick, esc, and quit)
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                playing = False
            
        if event.type == MOUSEBUTTONDOWN:
            clicking = True
        else:
            clicking = False
        
        if event.type == QUIT:
            playing = False

    # checks if you click on a square and whose turn it is
    if squarenum == 1 and clicking:
        if sq1.open:  
            if turn == "X":
                sq1image = pygame.image.load("resizedX.png")
                board[0] = "X"
                turn = "O"
            elif turn == "O":
                sq1image = pygame.image.load("resizedO.png")
                board[0] = "O"
                turn = "X"
            screen.blit(sq1image, (10, 10))        
            sq1.take()
    elif squarenum == 2 and clicking:
        if sq2.open:  
            if turn == "X":
                sq2image = pygame.image.load("resizedX.png")
                board[1] = "X"
                turn = "O"
            elif turn == "O":
                sq2image = pygame.image.load("resizedO.png")
                board[1] = "O"
                turn = "X"
            screen.blit(sq2image, (160, 10))        
            sq2.take()
    elif squarenum == 3 and clicking:
        if sq3.open:  
            if turn == "X":
                sq3image = pygame.image.load("resizedX.png")
                board[2] = "X"
                turn = "O"
            elif turn == "O":
                sq3image = pygame.image.load("resizedO.png")
                board[2] = "O"
                turn = "X"
            screen.blit(sq3image, (310, 10))        
            sq3.take()
    elif squarenum == 4 and clicking:
        if sq4.open:  
            if turn == "X":
                sq4image = pygame.image.load("resizedX.png")
                board[3] = "X"
                turn = "O"
            elif turn == "O":
                sq4image = pygame.image.load("resizedO.png")
                board[3] = "O"
                turn = "X"
            screen.blit(sq4image, (10, 160))        
            sq4.take()
    elif squarenum == 5 and clicking:
        if sq5.open:  
            if turn == "X":
                sq5image = pygame.image.load("resizedX.png")
                board[4] = "X"
                turn = "O"
            elif turn == "O":
                sq5image = pygame.image.load("resizedO.png")
                board[4] = "O"
                turn = "X"
            screen.blit(sq5image, (160, 160))        
            sq5.take()
    elif squarenum == 6 and clicking:
        if sq6.open:  
            if turn == "X":
                sq6image = pygame.image.load("resizedX.png")
                board[5] = "X"
                turn = "O"
            elif turn == "O":
                sq6image = pygame.image.load("resizedO.png")
                board[5] = "O"
                turn = "X"
            screen.blit(sq6image, (310, 160))        
            sq6.take()
    elif squarenum == 7 and clicking:
        if sq7.open:  
            if turn == "X":
                sq7image = pygame.image.load("resizedX.png")
                board[6] = "X"
                turn = "O"
            elif turn == "O":
                sq7image = pygame.image.load("resizedO.png")
                board[6] = "O"
                turn = "X"
            screen.blit(sq7image, (10, 310))        
            sq7.take()
    elif squarenum == 8 and clicking:
        if sq8.open:  
            if turn == "X":
                sq8image = pygame.image.load("resizedX.png")
                board[7] = "X"
                turn = "O"
            elif turn == "O":
                sq8image = pygame.image.load("resizedO.png")
                board[7] = "O"
                turn = "X"
            screen.blit(sq8image, (160, 310))        
            sq8.take()
    elif squarenum == 9 and clicking:
        if sq9.open:  
            if turn == "X":
                sq9image = pygame.image.load("resizedX.png")
                board[8] = "X"
                turn = "O"
            elif turn == "O":
                sq9image = pygame.image.load("resizedO.png")
                board[8] = "O"
                turn = "X"
            screen.blit(sq9image, (310, 310))        
            sq9.take()


    # checks for a winner using the board list
    if winner == "":
        # checks for x win
        if b1 == b2 == b3 == "X" or b4 == b5 == b6 == "X" or b7 == b8 == b9 == "X" or b1 == b4 == b7 == "X" or b2 == b5 == b8 == "X" or b3 == b6 == b9 == "X" or b1 == b5 == b9 == "X" or b7 == b5 == b3 == "X":
            winner = "X"
        # checks for o win
        if b1 == b2 == b3 == "O" or b4 == b5 == b6 == "O" or b7 == b8 == b9 == "O" or b1 == b4 == b7 == "O" or b2 == b5 == b8 == "O" or b3 == b6 == b9 == "O" or b1 == b5 == b9 == "O" or b7 == b5 == b3 == "O":
            winner = "O"
        # checks for a tie
        if " " not in board:
            playing = False
            print("Tie")
    
    if winner != "":
        playing = False
        print(f"{winner} wins!")
        
    print(board)
    pygame.display.flip()
