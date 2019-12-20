import pygame
import random
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Flappy Bird")

def text(message, font, size, x, y):
    '''
    Displays text on the screen

    text(message="String", font="String", size=int, x=int, y=int)
    '''
    font = pygame.font.SysFont(font, size)
    text = font.render(message, False, (0,0,0))
    win.blit(text,(x,y))
    pygame.display.update()

def resetgame():
    '''
    Resets all variables and objects

    Takes no args
    '''
    global birdy
    global birda
    global birdv
    global pipex1
    global pipex2
    global pipey1
    global pipey2
    global isPipe1Visible
    global isPipe2Visible
    global pipe1top
    global pipe1bot
    global pipe2top
    global pipe2bot
    global score
    global isLose
    global bird
    global pipe1
    global pipe2
    bird = Bird(50, 375, 3, 0)
    pipe1 = Pipe(500, 250, 7)
    pipe2 = Pipe(500, 250, 7)
    pipex1 = 500
    pipex2 = 500
    pipey1 = 250
    pipey2 = 250
    isPipe1Visible = True
    isPipe2Visible = False
    pipe1top = pygame.Rect(0,0,0,0)
    pipe1bot = pygame.Rect(0,0,0,0)
    pipe2top = pygame.Rect(0,0,0,0)
    pipe2bot = pygame.Rect(0,0,0,0)
    score = 0

    isLose = False


class Bird():

    def __init__(self, x, y, a, v):
        '''
        Creates bird object

        Bird(x=int, y=int, a=int, v=int)
        '''
        self.x = x
        self.y = y
        self.a = a
        self.v = v

    def draw(self, hasGravity=True):
        '''
        Draws bird object

        Bird().draw(hasGravity=bool)

        hasGravity is optional arg, default is True
        '''
        if hasGravity == True:
            self.v += self.a
            self.y += self.v
        pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, 50, 50))

    def jump(self, x):
        '''
        Makes bird jump by specified amount

        Bird().jump(x=int)
        '''
        self.v = x * -1

    def rect(self):
        '''
        Returns Bird object as pygame rect object

        Bird.rect() -> pygame.Rect
        '''
        return pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, 50, 50))

class Pipe():

    def __init__(self, x, y, v):
        '''
        Creates pipe object

        Pipe(x=int, y=int, v=int)
        '''
        self.x = x
        self.y = y
        self.v = v

    def draw(self):
        '''
        Draws pipe

        Pipe().draw()
        '''
        self.x -= self.v
        pygame.draw.rect(win, (0, 255, 0), (self.x, 0, 100, self.y))
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y + 250, 100, 750 - (self.y + 250)))

    def rect1(self):
        '''
        Returns top pipe as pygame Rect object

        Pipe().rect1() -> pygame.Rect
        '''
        return pygame.draw.rect(win, (0, 255, 0), (self.x, 0, 100, self.y))

    def rect2(self):
        '''
        Returns bottom pipe as pygame Rect object

        Pipe().rect2() -> pygame.Rect
        '''
        return pygame.draw.rect(win, (0, 255, 0), (self.x, self.y + 250, 100, 750 - (self.y + 250)))


resetgame()
run = False
while not run: #Wait for space to be pressed before starting
    win.fill((0, 153, 204))
    bird.draw(hasGravity=False)
    text("Press Space to Start", "Comic Sans MS", 30, 100, 300)
    keys = pygame.key.get_pressed()
    if keys[K_SPACE] == True:
        run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

while run: #Game starts here
    if not isLose:
        pygame.time.delay(30)

        win.fill((0, 153, 204)) #draws blue background

        keys = pygame.key.get_pressed()
        for event in pygame.event.get(): #This is just so it quits when you click the x
            if event.type == pygame.QUIT:
                run = False


        if keys[K_SPACE] == True: #jumping mechanic
            bird.jump(25)


        if isPipe1Visible == True:
            pipe1.draw()
            if pipe1.x == 52:
                pipe2.y = random.randint(50,450)
                pipe2.x = 500
                isPipe2Visible = True
                score += 1
            if pipe1.x <= 0:
                isPipe1Visible = False
                pipe1.x = 750
                pipe1.y = 0

        if isPipe2Visible == True:
            pipe2.draw()
            if pipe2.x == 52:
                pipe1.y = random.randint(50,450)
                pipe1.x = 500
                isPipe1Visible = True
                score +=1
            if pipe2.x <= 0:
                isPipe2Visible = False
                pipe2.x = 750
                pipe2.y = 0

        bird.draw()

        if bird.y <= 0 or bird.y >= 750 or bird.rect().colliderect(pipe1.rect1()) or bird.rect().colliderect(pipe1.rect2()) or bird.rect().colliderect(pipe2.rect1()) or bird.rect().colliderect(pipe2.rect2()): #losing mechanism
            isLose = True

        text(str(score), "Comic Sans MS", 60, 250, 20)


        pygame.display.update()
    else: #This runs when you lose
        win.fill((0, 153, 204))
        bird.draw()
        if isPipe2Visible:
            pipe2.draw()
        if isPipe1Visible:
            pipe1.draw()
        text("You lose! Press space to try again", "Comic Sans MS", 30, 10, 375)
        text(str(score), "Comic Sans MS", 60, 250, 20)
        pygame.display.update()
        isSpacePressed = False
        while not isSpacePressed:
            pygame.time.delay(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    isSpacePressed = True
            keys = pygame.key.get_pressed()
            if keys[K_SPACE] == True:
                resetgame()
                isSpacePressed = True




pygame.quit()
