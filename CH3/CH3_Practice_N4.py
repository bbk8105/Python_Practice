x1 = float(input("x1의 좌표: "))
y1 = float(input("y1의 좌표: "))
x2 = float(input("x2의 좌표: "))
y2 = float(input("y2의 좌표: "))

distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print("두점 사이의 거리 =", distance)
