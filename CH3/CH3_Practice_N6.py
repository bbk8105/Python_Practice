import turtle

t = turtle.Turtle()
t.shape("turtle")

x1 = float(input("x1 좌표: "))
y1 = float(input("y1 좌표: "))
x2 = float(input("x2 좌표: "))
y2 = float(input("y2 좌표: "))

t.up()
t.goto(x1, y1)
t.down()
t.goto(x2. y2)

xsum = (x1 - x2)**2
ysum = (y1 - y2)**2
total = (xsum + ysum)**0.5

print("두 점 사이의 거리 =", total)

