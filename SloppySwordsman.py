import pygame

import os


pygame.init()

pygame.mixer.init()
display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (222,41,16)
green = (0,255,0)
gold = (255, 222, 0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
car_width = 40
car_height = 54
UI =(149, 165, 166)
emerald =(39, 174, 96)
pomegranate =(192, 57, 43)
pom =(231, 76, 60)
em =(46, 204, 113)

pygame.display.set_caption('Ricey : Sloppy Swordsman')

#lobbybackground = pygame.image.load(os.path.join("data", 'lobby.png'))
clock = pygame.time.Clock()

still = pygame.image.load(os.path.join("data", 'back1.png'))


right = False
pause = False
left = False
top = False
bottom = False
yes = "no"
zero = 0


WD = False
AD = False
DD = False
SD = False
pygame.mixer.music.load(os.path.join("data", 'lobby.mp3'))
pygame.mixer.music.play(-1)


def game_loop():


    x = 0 + car_width
    y = display_height - car_height

    zero = 0
    gameExit = False

    left_images = []
    left_images.append( pygame.image.load(os.path.join("data", 'left1.png') ))
    left_images.append( pygame.image.load(os.path.join("data", 'left2.png') ))
    left_images.append( pygame.image.load(os.path.join("data", 'left3.png') ))
    right_images = []
    right_images.append( pygame.image.load(os.path.join("data", 'right1.png') ))
    right_images.append( pygame.image.load(os.path.join("data", 'right2.png') ))
    right_images.append( pygame.image.load(os.path.join("data", 'right3.png') ))

    left_current = 1
    right_current = 0

    left_walking = True
    left_walking_steps = 0
    left_current = (left_current + 1) % len(left_images)
    left_player = left_images[ left_current ]

    right_walking = False
    right_walking_steps = 0
    right_current = (right_current + 1) % len(right_images)
    right_player = right_images[ right_current ]
    onGround = False
    x_change = 0
    y_change = 0
    timer = 0




    while not gameExit:
        onGround = False
        if y == display_height - car_height:
            onGround = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and onGround == True:

                    if timer < 3 and y >= 506:
                        y_change = -10
                        y += y_change
                        y_change = -10
                        y += y_change
                        y_change = 0
                        timer += 1
                        if timer >= 3:
                             timer = 0
                        onGround = False



                if event.key == pygame.K_0:
                    print "null"
                elif event.key == pygame.K_a:

                    x_change = -8
                    left_walking = True
                    left_walking_steps = 5

                if event.key == pygame.K_2:
                    print "null"

                    

                elif event.key == pygame.K_d:
                    
                    x_change = 8
                    right_walking = True
                    right_walking_steps = 5
                if right_walking == True and event.key == pygame.K_LSHIFT:
                    x_change = 16
                    right_walking = True
                    right_walking_steps = 5
                if left_walking == True and event.key == pygame.K_LSHIFT:
                    x_change = -16
                    left_walking = True
                    left_walking_steps = 5



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                    left_current = 1
                    left_walking = False
                    right_walking = False
                if event.key == pygame.K_SPACE:
                    y_change = 0

        
                
        
        

        if left_walking == True:
        
            if left_walking_steps > 0:
                left_current = (left_current + 1) % len(left_images)
                left_player = left_images[ left_current ]
                
                
                if left_current == 3:
                    left_current 
            else:
                left_walking = False


        if right_walking == True:
        
            if right_walking_steps > 0:
                right_current = (right_current + 1) % len(right_images)
                right_player = right_images[ right_current ]
                
                
                
            else:
                right_walking = False

        left_walking == True
        gameDisplay.fill(UI)
        if left_walking == True:
            
            gameDisplay.blit(left_player,(x,y))

        elif right_walking == True:
            
            gameDisplay.blit(right_player,(x,y))
        else:
            gameDisplay.blit(still,(x,y))

        #gameDisplay.blit(lobbybackground,(0,0))
        if x > display_width- car_width:
            x -= 16
        if x < 0:
            x += 16


        x += x_change
        y += y_change

        if onGround == False:
            if y + 10 > display_height - car_height:
                print "po"
            else:

                y += 10

        if y >= 540:
            y = display_height - car_height
        print y
        xand = x + car_width
        careight = car_width/8
        mouse = pygame.mouse.get_pos()
        hitbox = pygame.Rect(x, y, car_width, car_height)
        leftRect = pygame.Rect(x, y, car_width/8 , car_height)
        rightRect = pygame.Rect(xand - careight, y, car_width/8 , car_height)
        pygame.draw.rect(gameDisplay, red,(x, y, careight , car_height))

        pygame.draw.rect(gameDisplay, gold,(xand - careight, y, car_width/8 , car_height))
        pygame.draw.rect(gameDisplay, black,(x + careight, y, car_width - careight - careight, car_height/8))
        pygame.draw.rect(gameDisplay, green,(x + careight, y + car_height, car_width - careight - careight, car_height/8))
        clock.tick(15)
        pygame.display.update()

game_loop()
