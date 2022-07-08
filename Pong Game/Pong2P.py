import pygame, sys, numpy, math, time

pygame.init()
width, height = 1000, 725
centerX, centerY = width/2, height/2
size = (width, height)
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()
pygame.display.set_caption("Pong - By:Spotech")

myFont = pygame.font.SysFont("monospace", 100)
Gold = (235, 200, 5)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)
Black = (0, 0, 0)
White = (255, 255, 255)

scoreL = 0
scoreR = 0

moveL = 0
moveR = 0

ballX = 0
ballY = 0

x_speed = 5
y_speed = -5

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)

screen.fill(Black)

rectleft = pygame.Rect(10, centerY-75+moveL, 25, 150)
rectright = pygame.Rect(width-40, centerY-75+moveR, 25, 150)
ball = pygame.Rect(centerX-10+ballX, centerY+ballY, 20, 20)

#Center Line
draw_dashed_line(screen, White, (centerX, 0), (centerX, height), dash_length=20)

#Ball
pygame.draw.rect(screen, White, ball)

#score
ScoreLeft = myFont.render(str(scoreL), False, White)
screen.blit(ScoreLeft, (centerX-70, 10))

ScoreRight = myFont.render(str(scoreR), False, White)
screen.blit(ScoreRight, (centerX+10, 10))

#Paddle
pygame.draw.rect(screen, White, rectleft) #Left
pygame.draw.rect(screen, White, rectright) #Right

pygame.display.flip()
clock.tick(fps)

time.sleep(2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            sys.exit()

    #Mouse Position
    mousePOS = pygame.mouse.get_pos()
    px = pygame.mouse.get_pos()[0]
    py = pygame.mouse.get_pos()[1]

    screen.fill(Black)

    rectleft = pygame.Rect(10, centerY-75+moveL, 25, 150)
    rectright = pygame.Rect(width-40, centerY-75+moveR, 25, 150)
    ball = pygame.Rect(centerX-10+ballX, centerY+ballY, 20, 20)

    #Center Line
    draw_dashed_line(screen, White, (centerX, 0), (centerX, height), dash_length=20)

    #Ball
    pygame.draw.rect(screen, White, ball)

    #score
    ScoreLeft = myFont.render(str(scoreL), False, White)
    screen.blit(ScoreLeft, (centerX-70, 10))

    ScoreRight = myFont.render(str(scoreR), False, White)
    screen.blit(ScoreRight, (centerX+10, 10))

    #Paddle
    pygame.draw.rect(screen, White, rectleft) #Left
    pygame.draw.rect(screen, White, rectright) #Right

    #Left Up
    if pygame.key.get_pressed()[pygame.K_w]:
        if (650+moveL) >= 360:
            moveL-=10
    
    #Left Down
    if pygame.key.get_pressed()[pygame.K_s]:
        if (650+moveL) <= (height+210):
            moveL+=10

    #Right Up
    if pygame.key.get_pressed()[pygame.K_UP]:
        if (650+moveR) >= 360:
            moveR-=10

    #Right Down
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        if (650+moveR) <= (height+210):
            moveR+=10

    ballX += x_speed
    ballY += y_speed

    if (490+ballX) == 0:
        scoreR+=1
        ballX, ballY = 0, 0
        x_speed = 0
        y_speed = 0
        moveR = 0
        moveL = 0
        x_speed = 5
        y_speed = 5

    if (490+ballX) == width:
        scoreL+=1
        ballX, ballY = 0, 0
        x_speed = 0
        y_speed = 0
        moveR = 0
        moveL = 0
        x_speed = -5
        y_speed = 5

    collideleft = pygame.Rect.colliderect(ball, rectleft)
    collideright = pygame.Rect.colliderect(ball, rectright)

    if collideleft:
        x_speed *= -1
        ballX += 10

    if collideright:
        x_speed *= -1
        ballX -= 10

    if ball.bottom==727:
        y_speed *= -1
        ballY -= 10

    if ball.top==2:
        y_speed *= -1
        ballY += 10
    
    #Update Frame
    pygame.display.flip()
    clock.tick(fps)