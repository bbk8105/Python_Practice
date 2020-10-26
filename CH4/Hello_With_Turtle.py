import turtle

t = turtle.Turtle()
n = turtle.textinput("", "이름을 입력하시오: ")

t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)


t.write("안녕하세요?" + n + "씨, 터틀 인사드립니다")
