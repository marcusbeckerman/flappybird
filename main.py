import pygame
import time
import random
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Flappy Bird")

def resetgame():
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
    birdy = 375
    birda = 3
    birdv = 0

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

resetgame()
run = True

while run:
    if not isLose:
        pygame.time.delay(30)

        win.fill((0, 153, 204)) #draws blue background
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        birdv += birda
        birdy += birdv

        if keys[K_SPACE] == True: #jumping mechanic
            birdv = -25


        if isPipe1Visible == True:
            pipex1 -= 7
            pipe1top = pygame.draw.rect(win, (0, 255, 0), (pipex1, 0, 100, pipey1))
            pipe1bot = pygame.draw.rect(win, (0, 255, 0), (pipex1, pipey1 + 250, 100, 750 - (pipey1 + 250)))
            if pipex1 == 52:
                pipey2 = random.randint(50,450)
                pipex2 = 500
                isPipe2Visible = True
                score += 1
            if pipex1 <= 0:
                isPipe1Visible = False
                pipe1top.move_ip(750, 0)
                pipe1bot.move_ip(750, 0)

        if isPipe2Visible == True:
            pipex2 -= 7
            pipe2top = pygame.draw.rect(win, (0, 255, 0), (pipex2, 0, 100, pipey2))
            pipe2bot = pygame.draw.rect(win, (0, 255, 0), (pipex2, pipey2 + 250, 100, 750 - (pipey2 + 250))) #ngl i have no idea how the fuck i did this my brain was just going off
            if pipex2 == 52:
                pipey1 = random.randint(50,450)
                pipex1 = 500
                isPipe1Visible = True
                score +=1
            if pipex2 <= 0:
                isPipe2Visible = False
                pipe2top.move_ip(750, 0)
                pipe2bot.move_ip(750, 0)

        bird = pygame.draw.rect(win, (255, 255, 0), (50, birdy, 50, 50)) #draws 'bird'

        if birdy <= 0 or birdy >= 750 or bird.colliderect(pipe1top) or bird.colliderect(pipe1bot) or bird.colliderect(pipe2top) or bird.colliderect(pipe2bot): #losing mechanism
            isLose = True

        font = pygame.font.SysFont("Comic Sans MS", 60)
        text = font.render(str(score), False, (0,0,0))
        win.blit(text,(250,20))


        pygame.display.update()
    else:
        win.fill((0, 153, 204))
        pygame.draw.rect(win, (255, 255, 0), (50, birdy, 50, 50))
        if isPipe2Visible:
            pygame.draw.rect(win, (0, 255, 0), (pipex2, pipey2 + 250, 100, 750 - (pipey2 + 250)))
            pygame.draw.rect(win, (0, 255, 0), (pipex2, 0, 100, pipey2))
        if isPipe1Visible:
            pygame.draw.rect(win, (0, 255, 0), (pipex1, pipey1 + 250, 100, 750 - (pipey1 + 250)))
            pygame.draw.rect(win, (0, 255, 0), (pipex1, 0, 100, pipey1))
        font = pygame.font.SysFont("Comic Sans MS", 30)
        text = font.render("You lose! Press space to try again", False, (0,0,0))
        win.blit(text,(10,375))
        font = pygame.font.SysFont("Comic Sans MS", 60)
        text = font.render(str(score), False, (0,0,0))
        win.blit(text,(250,20))
        pygame.display.update()
        isSpacePressed = False
        while not isSpacePressed:
            #print("isSpacePressed: " + str(isSpacePressed))
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
