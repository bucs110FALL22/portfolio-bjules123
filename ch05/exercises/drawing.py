import turtle
import math
import pygame
window = turtle.Screen() 
turt = turtle.Turtle()
turt.color('green')
num_sides = int(input("How many sides?"))
side_length = int(input("How long?"))
def drawEqShape(num_sides,side_length):
 angle = 360/num_sides
 for i in range(0, num_sides): 
    turtle.forward(side_length)
    turtle.right(angle)
   

drawEqShape()

