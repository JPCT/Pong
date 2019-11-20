import pygame,sys
from pygame.locals import *
import time


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



def main():
        #CONSTANTS
    DISTANCEPADELTOWALL = 35
    PADELMOVE = 1
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 600
    EFFECT_TOP = 0.05
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
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0 ,0)

    pygame.init()
    ventana = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ventana.fill(NEGRO)
    font = pygame.font.SysFont("ocraextended", 40)
    pygame.display.set_caption("PongPruebaCommit")

    #Sounds
    wallCollide = pygame.mixer.Sound('wallCollide.ogg')
    padelCollide = pygame.mixer.Sound('padelCollide.ogg')
    point = pygame.mixer.Sound('point.ogg')


    ball = balls(BLANCO, 100, 100, 10, 10, BALLSPEEDX, BALLSPEEDY)
    padel1 = padel(BLANCO, DISTANCEPADELTOWALL, 300, 100, 10)
    padel2 = padel(BLANCO, SCREEN_WIDTH - DISTANCEPADELTOWALL - 10, 300, 100, 10)

    running = True
    while running:
        for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False                          

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

            if rect1.colliderect(rectball):
                padelCollide.play()
                ball.speedX *= -1
            if rect2.colliderect(rectball):
                padelCollide.play()
                ball.speedX *= -1
                

            ventana.fill(NEGRO)

            if PLAYER1_SCORE == 5:
                win = font.render("PLAYER 1 WINS!!", True, BLANCO)
                ventana.blit(win, (3*SCREEN_WIDTH/9, SCREEN_HEIGHT/2,10,10))
                WINED = True
            elif PLAYER2_SCORE == 5:
                win = font.render("PLAYER 2 WINS!!", True, BLANCO)
                ventana.blit(win, (3*SCREEN_WIDTH/9, SCREEN_HEIGHT/2,10,10))
                WINED = True
                
                

            if WINED == False:

                scoreplayer1 = font.render(str(PLAYER1_SCORE), True, BLANCO)
                scoreplayer2 = font.render(str(PLAYER2_SCORE), True, BLANCO)
                ventana.blit(scoreplayer1, (SCREEN_WIDTH / 5,40,10,10))
                ventana.blit(scoreplayer2, ((3*SCREEN_WIDTH / 4),40,10,10))

                #BALL DRAW
                pygame.draw.rect(ventana, ball.color, rectball)

                #PADELS DRAW
                pygame.draw.rect(ventana, padel1.color, rect1)
                pygame.draw.rect(ventana, padel2.color, rect2)
                
                #MIDDLE LINES DRAW
                for i in range(0, SCREEN_HEIGHT, 20):
                    pygame.draw.line(ventana, BLANCO, (SCREEN_WIDTH/2, i), (SCREEN_WIDTH/2, i+10))



        else:
            ventana.fill(NEGRO)
            player1 = font.render("PLAYER 1", True, (r, g, b))
            player2 = font.render("PLAYER 2", True, (r, g, b))
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
    main()