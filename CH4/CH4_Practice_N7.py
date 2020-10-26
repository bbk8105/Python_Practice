import turtle

t = turtle.Turtle()

color_list = []

color = input("색상을 영어로 입력하시오: ")
color_list.append(color)
color = input("색상을 영어로 입력하시오: ")
color_list.append(color)
color = input("색상을 영어로 입력하시오: ")
color_list.append(color)

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.fd(100)
t.down()

t.fillcolor(color_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.fd(100)
t.down()

t.fillcolor(color_list[2])
t.begin_fill()
t.circle(50)
t.end_fill()
