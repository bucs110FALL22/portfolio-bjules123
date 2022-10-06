import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode()
(width,height) = pygame.display.get_window_size()
screen.fill("blue")
#print(width,height) #522 332
pygame.draw.circle(screen, "pink", (261, 161), 150)
pygame.display.flip()
pygame.draw.line(screen, "black", (0, 161), (522, 161),1)
pygame.draw.line(screen, "black", (261, 0), (261, 332),1)
pygame.display.flip()

#Part B
#x1 = random.randrange(0,522)
#y1 = random.randrange(0,322)

#print(x,y)
 #the distance formula
#is_in_circle = distance_from_center <=  (height * width)/2 #where length and width are the screen size
count = 0
while (count < 10):  
 count = count + 1
 x1 = random.randrange(0,522)
 y1 = random.randrange(0,322)
 distance_from_center = math.hypot(x1-261, y1-161)
 #pygame.draw.circle(screen, "blue",(x1,y1), 5)
 pygame.display.flip()
 if distance_from_center <=  150:
  pygame.draw.circle(screen, "green",(x1,y1), 5)
  pygame.time.wait(500)
  pygame.display.flip()
 else:
  pygame.draw.circle(screen, "red",(x1,y1), 5)
  pygame.time.wait(500)
  pygame.display.flip()
pygame.time.wait(3000)
print (count)
#Part C
screen = pygame.display.set_mode()
(width,height) = pygame.display.get_window_size()
screen.fill("blue")
#pygame.display.flip()

purpleSquare = pygame.draw.rect(screen,"purple",(171,131,60,60))
yellowSquare = pygame.draw.rect(screen,"yellow",(291,131,60,60))
pygame.display.flip()
input("Who do you think will win?")
a,b = pygame.mouse.get_pos()
def purpleChoice():
 if 171 < a < 231 and 131 < b < 191 and pygame.MOUSEBUTTONDOWN:
  print("Okay, purple!")
def yellowChoice():
 if 291 < a < 351 and 131 < b < 191 and pygame.MOUSEBUTTONDOWN:
  print("Okay, yellow!")

screen = pygame.display.set_mode()
(width,height) = pygame.display.get_window_size()
screen.fill("blue")
#print(width,height) #522 332
pygame.draw.circle(screen, "pink", (261, 161), 150)
pygame.display.flip()
pygame.draw.line(screen, "black", (0, 161), (522, 161),1)
pygame.draw.line(screen, "black", (261, 0), (261, 332),1)
pygame.display.flip()
pygame.time.wait(2000)

pointsy = 0
pointsp = 0
count = 1
while (count <= 10):  
 count = count + 1
 x3 = random.randrange(0,522)
 y3 = random.randrange(0,322)
 yellow_distance_from_center = math.hypot(x3-261, y3-161)
 yellow = pygame.draw.circle(screen, "yellow",(x3,y3), 5)
 if yellow_distance_from_center <=  150:
   pointsy = pointsy + 1
   pygame.time.wait(500)
   pygame.display.flip()
 x4 = random.randrange(0,522)
 y4 = random.randrange(0,322)
 purple_distance_from_center = math.hypot(x4-261, y4-161)
 purple = pygame.draw.circle(screen, "purple",(x4,y4), 5)
 if purple_distance_from_center <=  150:
   pointsp = pointsp + 1
   pygame.time.wait(500)
   pygame.display.flip()

#print(pointsy)
#print(pointsp)

if pointsy<pointsp :
  print("purple wins!")
elif pointsp<pointsy:
  print("yellow wins!")
#pygame.time.wait(2000)

pygame.display.flip()


