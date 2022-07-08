import pygame, random, sys, math, pathlib

pygame.init()

#Mouse Settings
pygame.mouse.set_cursor(pygame.cursors.broken_x)
#pygame.mouse.set_visible(False)

myFont = pygame.font.SysFont("monospace", 50)

#Set Window Size
width, height = 500, 500
size = (width, height)
screen = pygame.display.set_mode(size)

#Sets FPS of Window
fps = 60
clock = pygame.time.Clock()

sheep1 = "Sheep1.png"
sheep2 = "Sheep2.png"
sheep3 = "Sheep3.png"
sheep4 = "Sheep4.png"
sheep5 = "Sheep5.png"
sheep6 = "Sheep6.png"
sheep7 = "Sheep7.png"
sheep8 = "Sheep8.jpg"
sheep9 = "Sheep9.png"
sheep10 = "Sheep 10.png"
  
#Images
Sheep1 = pygame.image.load(sheep1)
Sheep2 = pygame.image.load(sheep2)
Sheep3 = pygame.image.load(sheep3)
Sheep4 = pygame.image.load(sheep4)
Sheep5 = pygame.image.load(sheep5)
Sheep6 = pygame.image.load(sheep6)
Sheep7 = pygame.image.load(sheep7)
Sheep8 = pygame.image.load(sheep8)
Sheep9 = pygame.image.load(sheep9)
Sheep10 = pygame.image.load(sheep10)

Wheat = pygame.image.load("Wheat.png")
HayBale = pygame.image.load("Haybale.png")
Sheers = pygame.image.load("Sheers.png")
  


  
#Wheat Location
wx = random.randrange(0, width)
wy = random.randrange(0, height)
  


  
#Score
score = 0
scored = False  


  
#y and x values
x = width
y = height



  
#colors
Gold = (235, 200, 5)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)
Black = (0, 0, 0)
White = (255, 255, 255)
Pulse = 0
Pulse1 = 255
  


  
while True:  

  scoreText = myFont.render(str(score), True, (0, 0, 0))
  screen.blit(scoreText, (10,10))
  
  #Check for any events that pygame has detected
  #Event - clicking anything/causing pygame to react
  #QUIT is clicking X on to of screen
  for event in pygame.event.get():
    if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
      sys.exit()
  


  
  #gets Mouse Possition
  mousePOS = pygame.mouse.get_pos()

  #Get x mouse POS
  px = pygame.mouse.get_pos()[0]

  #Get y mouse POS
  py = pygame.mouse.get_pos()[1]

  #gets Mouse Possition
  mouseSOP = (px + 100, py + 100)
  


  
  #Fills Screen Color
  screen.fill(Gold)
  


  
  #Distance
  dist = math.sqrt((px-wx)**2 + (py-wy)**2)

  #Colide
  Colide = dist <= 50

  #Checks if Wheat is toughing Sheep
  if pygame.mouse.get_pressed()[0]:
    if Colide:
      wx = random.randrange(0, width - 20)
      wy = random.randrange(0, height - 20)
      scored = True
      if score == 0:
        score += 1

      elif score%50 == 0:
        score += 10

      elif score != 0 and score%10 != 0 or score%50 != 0:
        score += 1

  #Background
  #screen.blit(image, (0, 0))

  if score > 800:
    #Sheep3
    screen.blit(pygame.transform.scale(Sheep10, (200, 200)), mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)
    #Wheat
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)
  
  #If the score is greater than 700
  elif score > 700:
    #Sheep3
    screen.blit(pygame.transform.scale(Sheep9, (200, 200)), mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)
    #Wheat
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)

  #If the score is greater than 600
  elif score > 600:
    #Sheep3
    screen.blit(pygame.transform.scale(Sheep8, (200, 200)), mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)
    #Wheat
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)
  
  #If the score is greater than 500
  elif score > 500:
    #Sheep3
    screen.blit(pygame.transform.scale(Sheep7, (200, 200)), mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)
    #Wheat
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)

  #If the score is greater than 400
  elif score > 400:
    #Sheep3
    screen.blit(pygame.transform.scale(Sheep6, (200, 200)), mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)
    #Wheat
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)
  
  #If the score is greater than 300
  elif score > 300:
    #Sheep3
    screen.blit(pygame.transform.scale(Sheep5, (200, 200)), mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)
    #Wheat
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)

  #If the score is greater than 200
  elif score > 200:
    #Sheep3
    screen.blit(pygame.transform.scale(Sheep4, (200, 200)), mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)
    #Wheat
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)
  
  #If the score is greater than 100
  elif score > 100:
    #Sheep3
    screen.blit(pygame.transform.scale(Sheep3, (200, 200)), mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)
    #Wheat
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)



  #If the score is a multiple of 50
  elif score%50 == 0 and score != 0:
    screen.blit(Sheep2, mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)

    #HayBale
    screen.blit(pygame.transform.scale(HayBale, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)
  

  #If the score is a multiple of 10
  elif score%10 == 0 and score != 0:
    screen.blit(Sheep2, mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)

    #Sheers
    screen.blit(pygame.transform.scale(Sheers, (100, 100)), (wx, wy, 100, 100))
    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)


  #If the score is normal
  elif score == 0 or score%10 != 0 or score%50 != 0:
    #Sheep
    screen.blit(Sheep1, mousePOS)
    #Circle
    #pygame.draw.circle(screen, Red, mouseSOP, 50)

    #Wheat
    screen.blit(pygame.transform.scale(Wheat, (100, 100)), (wx, wy, 100, 100))

    #Circle
    #pygame.draw.circle(screen, Green, (wx + 60, wy + 60), 50)
  



  #score
  if scored == True:
   pygame.display.set_caption("Score: " + str(score))
   #print("Score: "+ score)
  scored = False

  
  #Draws/Moves circle
  #pygame.draw.circle(screen, Red, mousePOS, 25)

  #Change Pulse
  #Pulse = (Pulse + 1) % 256
  #Pulse1 = (255 - Pulse)

  

  #Updates game frame
  text_surface = myFont.render(str(score), False, (0, 0, 0))
  screen.blit(text_surface, (width/2,height/4))
  pygame.display.flip()
  clock.tick(fps)
  


  
  #Check
  #print()
  #print()
  #print(mousePOS)
  #print("(" + str(wx) + ", " + str(wy) + ")")
  #print(mouseSOP)
  #print()
  #print()
  


  
  if wx > width or wy > height:
    wx = random.randrange(0, width - 100)
    wy = random.randrange(0, height - 100)