#License MIT 2016 Ahmad Retha

import pygame

##
# Game mode
#
WIDTH = 1366
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
pygame.key.set_repeat(50, 50)
pygame.init()
FSC = False

##
# Game consts
#
FONT = pygame.font.Font(None, 120)
FONT1 = pygame.font.Font(None, 30)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0 ,0, 255)
GRAY  = (100, 100, 100)
MODE_PLAY = 1
MODE_QUIT = 0
Game = 'stop'
FRAME_RATE = 120

##
# Game Vars
#
score_left = 0
score_right = 0
current_mode = MODE_PLAY
BALL_SPEED = 3
pos_x = int(0.5 * WIDTH)
speed_x = BALL_SPEED
pos_y = int(0.5 * HEIGHT)
speed_y = BALL_SPEED
BALL_COLOR = WHITE
BALL_RADIUS = 18
PADDLE_SPEED = 3
PADDLE_HEIGHT = 150
PADDLE_WIDTH = 20
PADDLE_LEFT_COLOR = WHITE
PADDLE_RIGHT_COLOR = WHITE
PADDLE_LEFT_X = int(0.5*PADDLE_WIDTH)
PADDLE_RIGHT_X = WIDTH - int(0.5*PADDLE_WIDTH) - PADDLE_WIDTH
paddle_left_y = int(0.5 * HEIGHT - 0.5 * PADDLE_HEIGHT)
paddle_right_y = paddle_left_y

##
# Game loop
#
while current_mode == MODE_PLAY:
    ##
    # Handle keyboard
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_mode = MODE_QUIT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            current_mode = MODE_QUIT

    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_UP]:
        paddle_right_y = paddle_right_y - PADDLE_SPEED
        if paddle_right_y < 0:
            paddle_right_y = 0;
    elif keysPressed[pygame.K_DOWN]:
        paddle_right_y = paddle_right_y + PADDLE_SPEED
        if paddle_right_y > (HEIGHT - PADDLE_HEIGHT):
            paddle_right_y = HEIGHT - PADDLE_HEIGHT
    if keysPressed[pygame.K_a]:
        paddle_left_y = paddle_left_y - PADDLE_SPEED
        if paddle_left_y < 0:
            paddle_left_y = 0
    elif keysPressed[pygame.K_z]:
        paddle_left_y = paddle_left_y + PADDLE_SPEED
        if paddle_left_y > (HEIGHT - PADDLE_HEIGHT):
            paddle_left_y = HEIGHT - PADDLE_HEIGHT
    elif keysPressed[pygame.K_F11]:
        if(FSC):
            screen = pygame.display.set_mode(SCREEN_SIZE)
            FSC=False
        else:
            screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN|pygame.RESIZABLE)
            FSC=True
    elif keysPressed[pygame.K_F1]:
        if(Game!='over'):
            Game='start'
            score_left = 0
            score_right = 0
    elif keysPressed[pygame.K_F2]:
        Game='stop'
        score_left = 0
        score_right = 0    
        
            
        

    ##
    # Draw arena and score
    #
    screen.fill(BLACK)
    pygame.draw.line(screen, GRAY, [int(0.5 * WIDTH), 0], [int(0.5 * WIDTH), HEIGHT], 1)
    text = FONT.render("%2s:%2s" % (str(score_left), str(score_right)), 5, GRAY)
    textpos = text.get_rect(centerx=WIDTH/2)
    screen.blit(text, textpos)
    text1 = FONT1.render("F1 : Play", 2, (0,100,100))
    textpos1 = text.get_rect(center=(WIDTH/2 - 400, 100))
    screen.blit(text1, textpos1)
    text1 = FONT1.render("F2 : Restart", 2, (0,100,100))
    textpos1 = text.get_rect(center=(WIDTH/2 - 400, 150))
    screen.blit(text1, textpos1)
    text1 = FONT1.render("F11 : FullScreen", 2, (0,120,120))
    textpos1 = text.get_rect(center=(WIDTH/2 - 400, 200))
    screen.blit(text1, textpos1)
    text1 = FONT1.render("Esc : Exit", 2, (0,120,120))
    textpos1 = text.get_rect(center=(WIDTH/2 - 400, 250))
    screen.blit(text1, textpos1)

    ##
    # Draw paddles
    #
    pygame.draw.rect(screen, PADDLE_LEFT_COLOR, (PADDLE_LEFT_X, paddle_left_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, PADDLE_RIGHT_COLOR, (PADDLE_RIGHT_X, paddle_right_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    ##
    # Move ball and update scores
    #

    if(score_right==5 or score_left==5):
        Game='over'


    if(Game=='over'):
        FONT2 = pygame.font.Font(None, 80)
        text2 = FONT2.render("Game Over", 2, (200,0,0))
        textpos2 = text.get_rect(centerx=WIDTH/2-88,centery=HEIGHT/2)
        screen.blit(text2, textpos2)
        FONT2 = pygame.font.Font(None, 50)
        a=0
        if(score_right>score_left):
            a=1
        if(a==1):
            text2 = FONT2.render("You Lose                    You Win", 2, (200,0,0))
            textpos2 = text.get_rect(centerx=WIDTH/2-140, centery=HEIGHT/2+120)
            screen.blit(text2, textpos2)
        if(a==0):
            text2 = FONT2.render("You Win                    You Lose", 2, (200,0,0))
            textpos2 = text.get_rect(centerx=WIDTH/2-140, centery=HEIGHT/2+120)
            screen.blit(text2, textpos2)    
            
        
    else: 
        if(Game=='start'):
            pos_x = pos_x + speed_x
            if pos_x > WIDTH:
                if pos_y > (0.5 * HEIGHT):
                    speed_y = abs(speed_y)
                else:
                    speed_y = -abs(speed_y)
                pos_x = int(0.5 * WIDTH)
                pos_y = int(0.5 * HEIGHT)
                score_left += 1
            elif pos_x < 0:
                if pos_y > (0.5 * HEIGHT):
                    speed_y = abs(speed_y)
                else:
                    speed_y = -abs(speed_y)
                pos_x = int(0.5 * WIDTH)
                pos_y = int(0.5 * HEIGHT)
                score_right += 1
            pos_y = pos_y + speed_y
            if pos_y > HEIGHT:
                speed_y = -speed_y
            elif pos_y < 0:
                speed_y = abs(speed_y)

        if(Game=='stop'):
            pos_x = int(0.5 * WIDTH)
            pos_y = int(0.5 * HEIGHT)
            
        pygame.draw.circle(screen, BALL_COLOR, [pos_x, pos_y], BALL_RADIUS)

        ##
        # Bounce ball off paddles
        #
        r = BALL_RADIUS
        if pos_x <= (PADDLE_LEFT_X + PADDLE_WIDTH)+r and pos_y >= paddle_left_y and pos_y <= (paddle_left_y + PADDLE_HEIGHT):
            pos_x = PADDLE_LEFT_X + PADDLE_WIDTH + r
            speed_x = abs(speed_x)
        elif pos_x >= PADDLE_RIGHT_X-r and pos_y >= paddle_right_y and pos_y <= (paddle_right_y + PADDLE_HEIGHT):
            pos_x = PADDLE_RIGHT_X-r
            speed_x = -speed_x

    ##
    # Tick-tock
    #
    pygame.display.update()
    clock.tick(FRAME_RATE)

pygame.quit()
