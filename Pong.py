import pygame,sys
from pygame.locals import *
import time

#CONSTANTS
PLAYER1_NAME = ''
PLAYER2_NAME = ''
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)

class balls():
    def __init__(self, color, x, y, height, width, speedX, speedY):
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speedX = speedX
        self.speedY = speedY


class padel():
    def __init__(self, color, x, y, height, width):
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width

def initWindow():
    global BLACK, WHITE, PLAYER1_NAME, PLAYER2_NAME, SCREEN_WIDTH, SCREEN_HEIGHT
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    screen.fill(BLACK)
    runninginitWindow = True
    pongImage = pygame.image.load("pongBackground.jpg")
    font = pygame.font.SysFont("ocraextended", 40)
    input_box1 = pygame.Rect((SCREEN_WIDTH/3) - 140, (SCREEN_HEIGHT - 200), 100, 50)
    input_box2 = pygame.Rect((SCREEN_WIDTH/3) - 140, (SCREEN_HEIGHT - 100), 100, 50)
    color_inactive = (193, 193, 193)
    color_active = WHITE
    color1 = color_inactive
    color2 = color_inactive
    active1 = False
    active2 = False
    text1 = 'Player 1'
    text2 = 'Player 2'

    while runninginitWindow:
        for event in pygame.event.get():
            if event.type == QUIT:
                runninginitWindow = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    PLAYER1_NAME = text1
                    PLAYER2_NAME = text2
                    runninginitWindow = False
                    main()
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    elif len(text1) < 9:
                        text1 += event.unicode
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    elif len(text2) < 9:
                        text2 += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box1.collidepoint(event.pos):
                    # Toggle the active variable.
                    active1 = not active1
                    if text1 == 'Player 1':
                        text1=''
                else:
                    active1 = False
                # Change the current color of the input box.
                color1 = color_active if active1 else color_inactive

                if input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active2 = not active2
                    if text2 == 'Player 2':
                        text2=''
                else:
                    active2 = False
                # Change the current color of the input box.
                color2 = color_active if active2 else color_inactive

        screen.fill(BLACK)

        screen.blit(pongImage, (256, 44))
        # Render the current text.
        txt_surface1 = font.render(text1, True, color1)
        # Resize the box if the text is too long.
        width1 = max(200, txt_surface1.get_width()+10)
        input_box1.w = width1
        # Blit the text.
        screen.blit(txt_surface1, (input_box1.x+5, input_box1.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color1, input_box1, 2)

        # Render the current text.
        txt_surface2 = font.render(text2, True, color2)
        # Resize the box if the text is too long.
        width2 = max(200, txt_surface2.get_width() + 10)
        input_box2.w = width2
        # Blit the text.
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color2, input_box2, 2)
        pygame.display.update()



def main():
    #CONSTANTS
    DISTANCEPADELTOWALL = 35
    PADELMOVE = 1
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 600
    EFFECT_TOP = 0.01
    EFFECT_BOT = 0.05
    BALLSPEEDX = 0.5
    BALLSPEEDY = 0.5
    PLAYER1_SCORE = 0
    PLAYER2_SCORE = 0
    STARTED = False
    WINED = False
    r = 255
    g = 255
    b = 255

    #COLORES
    WHITE = (255, 255, 255)
    BLACK = (0, 0 ,0)

    pygame.init()
    ventana = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ventana.fill(BLACK)
    font = pygame.font.SysFont("ocraextended", 40)
    pygame.display.set_caption("Pong")

    #Sounds
    wallCollide = pygame.mixer.Sound('wallCollide.ogg')
    padelCollide = pygame.mixer.Sound('padelCollide.ogg')
    point = pygame.mixer.Sound('point.ogg')


    ball = balls(WHITE, 100, 100, 10, 10, BALLSPEEDX, BALLSPEEDY)
    padel1 = padel(WHITE, DISTANCEPADELTOWALL, 300, 100, 5)
    padel2 = padel(WHITE, SCREEN_WIDTH - DISTANCEPADELTOWALL - 10, 300, 100, 5)

    running = True
    while running:
        for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            pygame.quit()
                            sys.exit()
                            

        if STARTED == True:
            ball.x += ball.speedX
            ball.y += ball.speedY
                
            keys = pygame.key.get_pressed()

            #Padel 1
            if keys[pygame.K_w]:
                if padel1.y > 0:
                    padel1.y -= PADELMOVE
                if rect1.colliderect(rectball) and ball.speedY > 0:
                    ball.speedY = ball.speedY * -1
                elif rect1.colliderect(rectball) and ball.speedY < 0 and ball.speedY > -3:
                    ball.speedY = ball.speedY - EFFECT_TOP


            if keys[pygame.K_s]:
                if padel1.y + padel1.height < SCREEN_HEIGHT:
                    padel1.y += PADELMOVE
                if rect1.colliderect(rectball) and ball.speedY < 0:
                    ball.speedY = ball.speedY * -1
                elif rect1.colliderect(rectball) and ball.speedY < 0 and ball.speedY < 3:
                    ball.speedY = ball.speedY + EFFECT_BOT

            #Padel 2
            if keys[pygame.K_UP]:
                if padel2.y > 0:
                    padel2.y -= PADELMOVE
                if rect2.colliderect(rectball) and ball.speedY > 0:
                    ball.speedY = ball.speedY * -1
                elif rect2.colliderect(rectball) and ball.speedY < 0 and ball.speedY > -3:
                    ball.speedY = ball.speedY - EFFECT_TOP

            if keys[pygame.K_DOWN]:
                if padel2.y + padel2.height < SCREEN_HEIGHT:
                    padel2.y += PADELMOVE
                if rect2.colliderect(rectball) and ball.speedY < 0:
                    ball.speedY = ball.speedY * -1
                elif rect2.colliderect(rectball) and ball.speedY < 0 and ball.speedY < 3:
                    ball.speedY = ball.speedY + EFFECT_BOT

            if ball.x + ball.width > SCREEN_WIDTH:
                point.play()
                PLAYER1_SCORE += 1
                ball.x = SCREEN_WIDTH/2
                ball.y = SCREEN_HEIGHT/2
                ball.speedX = BALLSPEEDX 
                ball.speedY = BALLSPEEDY
                BALLSPEEDY *= -1
            if ball.x < 0:
                point.play()
                PLAYER2_SCORE += 1
                ball.x = SCREEN_WIDTH/2
                ball.y = SCREEN_HEIGHT/2
                BALLSPEEDX = BALLSPEEDX *-1
                ball.speedY = BALLSPEEDY
                BALLSPEEDY *= -1
            if ball.y + ball.height > SCREEN_HEIGHT:
                wallCollide.play()
                ball.speedY = ball.speedY * -1
            if ball.y < 0:
                wallCollide.play()
                ball.speedY = ball.speedY * -1
                


            rect1 = Rect(padel1.x, padel1.y, padel1.width, padel1.height)
            rect2 = Rect(padel2.x, padel2.y, padel2.width, padel2.height)
            rectball = Rect(ball.x, ball.y, ball.width, ball.height)

            if Rect(padel1.x, padel1.y, 0, padel1.height).colliderect(rectball):
                padelCollide.play()
                ball.speedX *= -1
            if Rect(padel2.x, padel2.y, 0, padel2.height).colliderect(rectball):
                padelCollide.play()
                ball.speedX *= -1
                

            ventana.fill(BLACK)

            if PLAYER1_SCORE == 5:
                win = font.render("PLAYER 1 WINS!!", True, WHITE)
                ventana.blit(win, (3*SCREEN_WIDTH/9, SCREEN_HEIGHT/2,10,10))
                WINED = True
            elif PLAYER2_SCORE == 5:
                win = font.render("PLAYER 2 WINS!!", True, WHITE)
                ventana.blit(win, (3*SCREEN_WIDTH/9, SCREEN_HEIGHT/2,10,10))
                WINED = True
                
                

            if WINED == False:

                scoreplayer1 = font.render(str(PLAYER1_SCORE), True, WHITE)
                scoreplayer2 = font.render(str(PLAYER2_SCORE), True, WHITE)
                ventana.blit(scoreplayer1, (SCREEN_WIDTH / 5,40,10,10))
                ventana.blit(scoreplayer2, ((3*SCREEN_WIDTH / 4),40,10,10))

                #BALL DRAW
                pygame.draw.rect(ventana, ball.color, rectball)

                #PADELS DRAW
                pygame.draw.rect(ventana, padel1.color, rect1)
                pygame.draw.rect(ventana, padel2.color, rect2)
                
                #MIDDLE LINES DRAW
                for i in range(0, SCREEN_HEIGHT, 20):
                    pygame.draw.line(ventana, WHITE, (SCREEN_WIDTH/2, i), (SCREEN_WIDTH/2, i+10))



        else:
            ventana.fill(BLACK)
            global PLAYER1_NAME, PLAYER2_NAME
            player1 = font.render(PLAYER1_NAME, True, (r, g, b))
            player2 = font.render(PLAYER2_NAME, True, (r, g, b))
            ventana.blit(player1, (SCREEN_WIDTH / 6, SCREEN_HEIGHT/2,10,10))
            ventana.blit(player2, ((3*SCREEN_WIDTH / 5), SCREEN_HEIGHT/2 ,10,10))
            

            if r > 170:
                timer = font.render("3", True, (r, g, b))
                ventana.blit(timer, (SCREEN_WIDTH / 2, SCREEN_HEIGHT/2,50,50))
            elif r > 85:
                timer = font.render("2", True, (r + 30, g + 30, b + 30))
                ventana.blit(timer, (SCREEN_WIDTH / 2, SCREEN_HEIGHT/2,50,50))
            elif r > 20:
                timer= font.render("1", True, (r + 30, g + 30, b + 30))
                ventana.blit(timer, (SCREEN_WIDTH / 2, SCREEN_HEIGHT/2,50,50))
            elif r > 0:
                timer = font.render("0", True, (r + 30, g + 30, b + 30))
                ventana.blit(timer, (SCREEN_WIDTH / 2, SCREEN_HEIGHT/2,50,50))

            r -= 1
            g -= 1
            b -= 1

            if r == 0 and g == 0 and b == 0:
                STARTED = True
            else:
                time.sleep(0.01)


        pygame.display.update()
        if WINED == True:
            time.sleep(2)
            r = 255
            g = 255
            b = 255
            PLAYER1_SCORE = 0
            PLAYER2_SCORE = 0
            ball.speedY = BALLSPEEDY
            ball.speedX = BALLSPEEDX
            STARTED = False
            WINED = False

if __name__ == "__main__":
    initWindow()
    main()