# 다음과 같은 그림을 그리는 프로그램을 완성하시오.
# 이 때 작은 사각형의 한 변의 길이를 side 변수에 저장하고 거북이가 회전하는 각도 angle 변수에 저장한다.

import turtle

t = turtle.Turtle()
t.shape("turtle")

side = 100
angle = 90

t.fd(side)
t.lt(angle)
t.fd(side)
t.lt(angle)
t.fd(side)
t.lt(angle)
t.fd(side * 2)
t.lt(angle)
t.fd(side)
t.lt(angle)
t.fd(side)
t.lt(angle)
t.fd(side * 2)
t.lt(angle)
t.fd(side)
t.lt(angle)
t.fd(side)
t.lt(angle)
t.fd(side * 2)
t.lt(angle)
t.fd(side)
t.lt(angle)
t.fd(side)

t.up()
t.goto(0, 0)
t.down()

