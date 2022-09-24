import turtle #1. import modules
import random
import pygame
import math

#Part A

window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#5. Your PART A code goes here
michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))
leonardo.goto(-100,-20)

for i in range(10):
    michelangelo.forward(random.randrange(1,10))
    leonardo.forward(random.randrange(1,10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()
window.fill("red")

#pygame.draw.polygon(window, "black", [(100, 100), (100, 200), (200, 200),(200,100)])
num_sides = 3
side_length = 100
offset = 100
coords = []


for i in range(num_sides):  
 theta = (2.0 * math.pi * i) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append((x,y))

window.fill("blue")
pygame.draw.polygon(window, "black", coords)
pygame.display.flip()
pygame.time.wait(1000)



num_sides = 4
side_length = 100
offset = 100
coords = []

for i in range(num_sides):  
 theta = (2.0 * math.pi * i) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append((x,y))

window.fill("blue")
pygame.draw.polygon(window, "black", coords)
pygame.display.flip()
pygame.time.wait(1000)



num_sides = 6
side_length = 100
offset = 100
coords = []

for i in range(num_sides):  
 theta = (2.0 * math.pi * i) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append((x,y))

window.fill("blue")
pygame.draw.polygon(window, "black", coords)
pygame.display.flip()
pygame.time.wait(1000)


num_sides = 9
side_length = 100
offset = 100
coords = []

for i in range(num_sides):  
 theta = (2.0 * math.pi * i) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append((x,y))

window.fill("blue")
pygame.draw.polygon(window, "black", coords)
pygame.display.flip()
pygame.time.wait(1000)



num_sides = 360
side_length = 100
offset = 100
coords = []

for i in range(num_sides):  
 theta = (2.0 * math.pi * i) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append((x,y))

window.fill("blue")
pygame.draw.polygon(window, "black", coords)
pygame.display.flip()
pygame.time.wait(1000)