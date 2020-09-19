import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 500:
    t.fd(length)
    t.pencolor(colors[length%6])
    t.rt (89)
    length += 5
