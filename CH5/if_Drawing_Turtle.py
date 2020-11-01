import turtle

t = turtle.Turtle()

s = turtle.textinput("", "도형을 입력하세요(사각형, 삼각형, 원)")
v = turtle.textinput("", "세로: ")
h = turtle.textinput("", "가로: ")

v = int(v)
h = int(h)

if s == "사각형" :
    t.fd(h)
    t.lt(90)
    t.fd(v)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(v)
    t.lt(90)
elif s == "삼각형" :
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
else :
    t.circle(50)
