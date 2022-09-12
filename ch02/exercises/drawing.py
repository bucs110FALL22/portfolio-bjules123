import turtle
my_turtle = turtle.Turtle()
my_screen = turtle.Screen()


sides = int(input("Enter a the number of sides "))
length = int(input("Enter the length of each side "))
n=sides
angle = 360/n
turtle.shape("turtle")
turtle.color("blue")
for i in range(0, n): 
    n = [sides, int(sides)] 
    turtle.forward(length)
    turtle.right(angle)


window = turtle.Screen()

window.exitonclick()