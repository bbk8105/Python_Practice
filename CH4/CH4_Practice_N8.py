import turtle

t = turtle.Turtle()

t.shape("turtle")

x_list = []
y_list = []

x = int(input("x1의 좌표: "))
y = int(input("y1의 좌표: "))
x_list.append(x)
y_list.append(y)

x = int(input("x2의 좌표: "))
y = int(input("y2의 좌표: "))
x_list.append(x)
y_list.append(y)

x = int(input("x3의 좌표: "))
y = int(input("y3의 좌표: "))
x_list.append(x)
y_list.append(y)

t.goto(x_list[0], y_list[0])
t.goto(x_list[1], y_list[1])
t.goto(x_list[2], y_list[2])



