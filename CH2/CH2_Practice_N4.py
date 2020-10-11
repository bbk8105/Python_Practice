#원의 반지름을 변수 radius에 저장한다.(초기값은 50)
#radius 변수를 20씩 증가시키면서 (0, 0), (100, 0), (200, 0) 좌표에 원을 3개 그려보자
#터틀 그래픽을 사용하고 반복문은 사용하지 않는다.

import turtle

t = turtle.Turtle()
t.shape("turtle")

radius = 50 # radius 변수 선언 

t.circle(radius)
radius = radius + 20
t.up()
t.goto(100, 0)
t.down()
t.circle(radius)
radius = radius + 20
t.up()
t.goto(200, 0)
t.down()
t.circle(radius)
