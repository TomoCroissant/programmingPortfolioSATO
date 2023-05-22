# By Tomo Sato, Ian Turner, reid Nguyen

import pygame, sys
from pygame.locals import QUIT
from Player import Player
from NPC import NPC
from Bullet import Bullet

player = Player()
roomNum = 1
text = False
play = True
endScreen = False
canShoot = True
boomerangHit = False
frameRate = pygame.time.Clock()
baseFPS = 60
score = 0
highScore = 0
enemyTimer = 0

#creates sprite image
spriteSize = 100
playerSprite = pygame.image.load('james2.png')
playerSprite = pygame.transform.scale(playerSprite, (spriteSize, spriteSize))

#create boomerang image
boomerang1 = pygame.image.load('boomerang1.png')
boomerang1 = pygame.transform.scale(boomerang1, (50, 50))

enemyImage = pygame.image.load('shroom.png')
enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))

#creates images of rooms
room1 = pygame.image.load('room1.png') #shroom
room1 = pygame.transform.scale(room1, (1280, 1280))
room2 = pygame.image.load('subManMap.png') #underwater
room2 = pygame.transform.scale(room2, (1280, 1280))
room3 = pygame.image.load('chrisMap.png') #swamp
room3 = pygame.transform.scale(room3, (1280, 1280))
room4 = pygame.image.load('FlymanMap.png') #barren
room4 = pygame.transform.scale(room4, (1280, 1280))
room5 = pygame.image.load('EvilJamesMap.png') #volcano
room5 = pygame.transform.scale(room5, (1280, 1280))
room6 = pygame.image.load('deessert.png') #desert
room6 = pygame.transform.scale(room6, (1280, 1280))
room7 = pygame.image.load('void.png') #void
room7 = pygame.transform.scale(room7, (1280, 1280))
room8 = pygame.image.load('tundra.png') #tundra
room8 = pygame.transform.scale(room8, (1280, 1280))
room9 = pygame.image.load('AlienMap1.png') #alien
room9 = pygame.transform.scale(room9, (1280, 1280))
room10 = pygame.image.load('HeavenMap2a.png') #angel
room10 = pygame.transform.scale(room10, (1280, 1280))

#updates SaveData.txt file with saved highscore
def makeSave():
  save = open("SaveData.txt", "w")
  save.write(str(highScore))
  save.close()

#accesses high score
save = open("SaveData.txt", "r")
contents = save.readlines()
save.close()
highScore = int(contents[0])
print("High Score:", contents[0])

#chooses which image to render based on roomNum
def drawRoom():
  if(roomNum == 1):
    screen.blit(room1, (0, 0))
  elif(roomNum == 2):
    screen.blit(room2, (0, 0))
  elif(roomNum == 3):
    screen.blit(room3, (0, 0))
  elif(roomNum == 4):
    screen.blit(room4, (0, 0))
  elif(roomNum == 5):
    screen.blit(room5, (0, 0))
  elif(roomNum == 6):
    screen.blit(room6, (0, 0))
  elif(roomNum == 7):
    screen.blit(room7, (0, 0))
  elif(roomNum == 8):
    screen.blit(room8, (0, 0))
  elif(roomNum == 9):
    screen.blit(room9, (0, 0))
  elif(roomNum == 10):
    screen.blit(room10, (0, 0))
  else:
    screen.blit(room1, (0, 0))
    

pygame.init()
screen = pygame.display.set_mode((1280, 1280))
clock = pygame.time.Clock()
running = False
B1 = Bullet(-10, -10, pygame.Vector2(-10, -10))
Enemies = []

#draws image of player to screen
def drawPlayer(x, y):
  screen.blit(playerSprite, (x - spriteSize / 2, y - spriteSize / 2))





#main menu
while play:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
      pygame.quit()
      sys.exit()
  
  screen.fill("blue")
  font = pygame.font.Font('FontdinerSwanky.ttf', 32)
  text = font.render('Press mouse to begin. Highscore: ' + str(highScore), True , "green", "blue")
  textRect = text.get_rect()
  textRect.center = (1280 // 2, 1280 // 2)
  screen.blit(text, textRect)
  fontb = pygame.font.Font('FontdinerSwanky.ttf', 32)
  textb = font.render('Alptraum von James', True , "green", "blue")
  textRectb = text.get_rect()
  textRectb.center = (1280 // 2, 1280 // 4)
  screen.blit(textb, textRectb)
  fontc = pygame.font.Font('FontdinerSwanky.ttf', 32)
  textc = font.render('Du hast uns sehr wütend gemacht!', True , "green", "blue")
  textRectc = text.get_rect()
  textRectc.center = (1280 // 2, 1000)
  screen.blit(textc, textRectc)
  pygame.display.update()
  #Check for mouse press to start game. Reset parameters on start.
  if (pygame.mouse.get_pressed() == (1, 0, 0)):
    for var in Enemies:
          Enemies.remove(var)
    running = True
    score = 0
    roomNum = 1
    enemyImage = pygame.image.load('shroom.png')
    enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
    player.health = 10
    B1.xpos = 640
    B1.ypos = 640

  #main loop
  while running:
    for event in pygame.event.get():
      if event.type == QUIT:
        running = False
        pygame.quit()
        sys.exit()
  
    frameRate.tick(baseFPS)
    drawRoom()
  
    player_pos = pygame.Vector2(player.xpos, player.ypos)
    
    drawPlayer(player_pos.x, player_pos.y)

    #Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y > 1:
      player.ypos -= 0.5 * (1 + frameRate.get_time())
    if keys[pygame.K_s] and player_pos.y < 1279:
      player.ypos += 0.5 * (1 + frameRate.get_time())
    if keys[pygame.K_a] and player_pos.x > 1:
      player.xpos -= 0.5 * (1 + frameRate.get_time())
    if keys[pygame.K_d] and player_pos.x < 1279:
      player.xpos += 0.5 * (1 + frameRate.get_time())
  
  
  
    #Add new enemies when timer ends
    if (enemyTimer <= 0):
      Enemies.append(
        NPC((pygame.mouse.get_pos()[0]), (pygame.mouse.get_pos()[1]),player_pos))
      enemyTimer = 1000
    if (pygame.mouse.get_pressed() == (1, 0, 0) and canShoot):
      
      B1 = Bullet((pygame.mouse.get_pos()[0]), (pygame.mouse.get_pos()[1]),player_pos)
      canShoot = False
  
    B1.move()
    B1.frameRate.tick(baseFPS)
    screen.blit(boomerang1, (B1.xpos, B1.ypos))
    if (B1.ypos >+ 1280 or B1.ypos <+ 0 or B1.xpos >+ 1280 or B1.xpos <+ 0):
      if (boomerangHit == False):
        B1.invert(player_pos)
        boomerangHit = True
      else:
        
        boomerangHit = False
    for var in Enemies:
      NPC.move(var)
      var.playerPos = player_pos
      var.frameRate.tick(baseFPS)
      screen.blit(enemyImage, (var.xpos, var.ypos))
      if(player.colDet(var)):
        player.health -= 1
        var.xpos = 1280
        B1.invert(player_pos)
        boomerangHit = True
        if player.health == 0:
          player.xpos = 0
          player.ypos = 0
          running = False

      #Collision detection for bullet, set level, enemy type, room and score
      if (var.colDet(B1)):
            Enemies.remove(var)
            score += 1
            if(highScore < score):
              highScore = score
            makeSave()

            if(score >= 50):
              running = False
              endScreen = True

            elif(score >= 45):
              roomNum = 10
              enemyImage = pygame.image.load('Angel.png')

            elif(score >= 40):
              roomNum = 9
              enemyImage = pygame.image.load('Alien1.png')

            elif(score >= 35):
              roomNum = 8
              enemyImage = pygame.image.load('Yeti.png')
              
              
            elif(score >= 30):
              roomNum = 7
              enemyImage = pygame.image.load('void crem.png')
              
              
            elif(score >= 25):
              roomNum = 6
              enemyImage = pygame.image.load('deom cerab.png')
              
            elif(score >= 20):
              roomNum = 5
              enemyImage = pygame.image.load('EvilJames.png')
              
            elif(score >= 15):
              roomNum = 4
              enemyImage = pygame.image.load('Fly Man.png')
              
            elif(score >= 10):
              roomNum = 3
              enemyImage = pygame.image.load('ChrisFullBody.png')
              
            elif(score >= 5):
              roomNum = 2
              enemyImage = pygame.image.load('subarine man.png')
              
            else:
              enemyImage = pygame.image.load('shroom.png')
              
              roomNum = 1

    #renders and scales enemy image
    enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
    
    #renders score box
    font2 = pygame.font.Font('FontdinerSwanky.ttf', 32)
    text2 = font2.render('Score: ' + str(score), True, "green", "blue")
    textRect2 = text2.get_rect()
    textRect2.center = (1000, 28)
    screen.blit(text2, textRect2)
    
    #renders health box
    fonta = pygame.font.Font('FontdinerSwanky.ttf', 32)
    texta = fonta.render("Health: " + str(player.health), True, "green", "blue" )
    textRecta = texta.get_rect()
    textRecta.center = (800, 28)
    screen.blit(texta, textRecta)

    #renders high score box
    font3 = pygame.font.Font('FontdinerSwanky.ttf', 32)
    text3 = font3.render('High Score: ' + str(highScore), True, "green", "blue")
    textRect3 = text3.get_rect()
    textRect3.center = (550, 28)
    screen.blit(text3, textRect3)
    
    pygame.display.update()
    enemyTimer -= (1 + frameRate.get_time())

  #End screen and dialogue
  while endScreen:
    for event in pygame.event.get():
      if event.type == QUIT:
        running = False
        pygame.quit()
        sys.exit()
    screen.fill("blue")
    font = pygame.font.Font('FontdinerSwanky.ttf', 16)
    text3 = font.render('Pilzmann: Du wirst niemals frei von mir sein.', True, "green", "blue")
    text4 = font.render('U-Boot-Mann: Ich bringe dich immer runter.', True, "green", "blue")
    text5 = font.render('Chris: Versuch und Versuch, du wirst mich nie vergessen.', True, "green", "blue")
    text6 = font.render('Fliegenmann: Die Welt ist immer düster.', True, "green", "blue")
    text7 = font.render('Böser James: Du bist nichts ohne mich.', True, "green", "blue")
    text8 = font.render('James: Nein. Du wirst nicht zu mir zurückkommen.', True, "red", "blue")
    textRect3 = text3.get_rect()
    textRect3.center = (640 // 2, 100)
    screen.blit(text3, textRect3)
    textRect4 = text4.get_rect()
    textRect4.center = (640 // 2, 200)
    screen.blit(text4, textRect4)
    textRect5 = text5.get_rect()
    textRect5.center = (640 // 2, 300)
    screen.blit(text5, textRect5)
    textRect6 = text6.get_rect()
    textRect6.center = (640 // 2, 400)
    screen.blit(text6, textRect6)
    textRect7 = text7.get_rect()
    textRect7.center = (640 // 2, 500)
    screen.blit(text7, textRect7)
    textRect8 = text8.get_rect()
    textRect8.center = (640 // 2, 600)
    screen.blit(text8, textRect8)
    pygame.display.update()
    
    if (pygame.mouse.get_pressed() == (1, 0, 0)):
      for var in Enemies:
          Enemies.remove(var)
      enemyImage = pygame.image.load('shroom.png')
      enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
      roomNum = 1
      score = 0
      endScreen = False
      running = True