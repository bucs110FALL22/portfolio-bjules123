import turtle
window = turtle.Screen()
window.bgcolor("lightblue")
turt = turtle.Turtle()

a = -10
b = 20
z = 0
x = 100
y = 90
def draw_to_right(a, s):
  return a + s
right = draw_to_right(a, 125)
def draw_down(b, s):
  return b - s
down = draw_down(b, 150)
def main():
 circledrawing(turt)
 square_pos(a,b)
 draw_triangle()
def circledrawing(turt):
  turt.penup()
  turt.goto(0, -100)
  turt.pendown()
  turt.circle(100)
def square_pos(a,b):
  turt.penup()
  turt.goto(a,b)
  turt.pendown()
  draw_square(x,y)
  turt.penup()
  turt.goto(right,b)
  turt.pendown()
  draw_square(x,y)
  turt.penup()
  turt.goto(a,down)
  turt.pendown()
  draw_square(x,y)
  turt.penup()
  turt.goto(right,down)
  turt.pendown()
  draw_square(x,y)
def draw_square(x,y):
  for z in range(4):
   turt.left(y)
   turt.forward(x)
   z = z + 1
def draw_triangle():
  turt.penup()
  turt.goto(-90,-55)
  turt.pendown()
  turt.forward(175)
  turt.left(120)
  turt.forward(175) 
  turt.left(120)
  turt.forward(175)
  
main()

window.exitonclick()
