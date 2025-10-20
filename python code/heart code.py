import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
heart = turtle.Turtle()
heart.color("red")
heart.pensize(3)
heart.speed(1)

# Draw heart shape
heart.begin_fill()
heart.left(140)
heart.forward(180)
heart.circle(-90, 200)
heart.left(120)
heart.circle(-90, 200)
heart.forward(180)
heart.end_fill()

# Hide turtle and keep window open
heart.hideturtle()
turtle.done()
