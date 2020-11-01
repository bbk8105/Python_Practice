import random

options = ["왼쪽", "중앙", "오른쪽"]

cpu = random.choice(options)
user = input("어디를 수비하시겠어요?(왼쪽, 중앙, 오른쪽): ")

if user == cpu :
    print("수비에 성공하셨습니다")
else :
    print("수비에 실패했습니다")

