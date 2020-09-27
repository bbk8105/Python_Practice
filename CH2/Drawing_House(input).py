import turtle

t = turtle.Turtle()

size = int(input("집의 크기를 몇으로 할까요: "))


#지붕 그리기
t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)

#벽 그리기
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
