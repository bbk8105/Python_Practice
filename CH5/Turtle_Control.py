import turtle

t = turtle.Turtle()

t.shape("turtle")
t.shapesize(3, 3)

while True :
    command = input("명령을 입력하시오.(1이나 r): ")

    if command == "1" :
        t.lt(90)
        t.fd(100)

    if command == "r" :
        t.rt(90)
        t.fd(100)
        
