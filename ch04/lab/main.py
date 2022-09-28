import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode()
(width,height) = pygame.display.get_window_size()
screen.fill("blue")
print(width,height) #522 332
pygame.draw.circle(screen, "pink", (261, 161), 150)
pygame.display.flip()
pygame.draw.line(screen, "black", (0, 161), (522, 161),1)
pygame.draw.line(screen, "black", (261, 0), (261, 332),1)
pygame.display.flip()

#Part B
x1 = random.randrange(0,522)
y1 = random.randrange(0,322)

#print(x,y)
pygame.draw.circle(screen, "purple",(x1,y1), 5)
pygame.display.flip()
distance_from_center = math.hypot(x1-261, y1-161) #the distance formula
#is_in_circle = distance_from_center <=  (height * width)/2 #where length and width are the screen size

if distance_from_center <=  150:
 pygame.draw.circle(screen, "green",(x1,y1), 5)
 pygame.display.flip()
else:
 pygame.draw.circle(screen, "red",(x1,y1), 5)
 pygame.display.flip()

pygame.time.wait(2000)

