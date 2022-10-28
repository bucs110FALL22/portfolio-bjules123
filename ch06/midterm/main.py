import turtle


A = -10
B = 20
X = 100
Y = 90


def draw_to_right(A, s):
  '''
   A: (constant) x-coordinate for squares
   s: (variable) varible added to A for coordinate to shift 
   right
  '''
  return A + s
def draw_down(B, s):
  '''
   B: (constant) y-coordinate for squares
   s: (variable) varible added to A for coordinate to shift 
   down
  '''
  return B - s
def main():
 turt = turtle.Turtle()
 window = turtle.Screen()
 window.bgcolor("lightblue")
 right = draw_to_right(A, 125)
 down = draw_down(B,150)
 circledrawing(turt)
 square_pos(A,B, turt, down, right)
 draw_triangle(turt)
 window.exitonclick()
def circledrawing(turt):
  '''
   turt: (variable) turtle
  '''
  turt.penup()
  turt.goto(0, -100)
  turt.pendown()
  turt.circle(100)
def square_pos(A,B, turt, down, right):
  '''
   A: (constant) x-coordinate for squares
   B: (constant) y-coordinate for squares
   turt: (variable) turtle
   down: (variable) coordinate to move down from A
   right: (variable) coordinate to move to the right from B
  '''
  turt.penup()
  turt.goto(A,B)
  turt.pendown()
  draw_square(X,Y,turt)
  turt.penup()
  turt.goto(right,B)
  turt.pendown()
  draw_square(X,Y,turt)
  turt.penup() 
  turt.goto(A,down)
  turt.pendown()
  draw_square(X,Y,turt)
  turt.penup()
  turt.goto(right,down)
  turt.pendown()
  draw_square(X,Y,turt)
def draw_square(X,Y,turt):
  '''
   X: (constant) foward distance
   Y: (constant) left angle
   turt: (variable) turtle
  '''
  z = 0
  for z in range(4):
   turt.left(Y)
   turt.forward(X)
   z = z + 1
def draw_triangle(turt):
  '''
   turt: (variable) turtle
  '''
  turt.penup()
  turt.goto(-90,-55)
  turt.pendown()
  turt.forward(175)
  turt.left(120)
  turt.forward(175) 
  turt.left(120)
  turt.forward(175)
  
main()


