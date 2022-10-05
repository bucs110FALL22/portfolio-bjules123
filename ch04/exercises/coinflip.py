import turtle
import random
window = turtle.Screen() 
window.bgcolor('lightgreen')
turt = turtle.Turtle()
turt.color('orange')
turt.shape('turtle')
turt.up()
def cointoss():
   return random.choice(["Heads", "Tails"])


while (turt.xcor(),200) and (turt.ycor(),200) :
 cointoss()
 if cointoss() == "Heads":
   turt.left(90)
   turt.forward(50)
 elif cointoss() == "Tails":
  turt.right(90)
  turt.forward(50)
window.exitonclick()

