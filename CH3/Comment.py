# 사용자로부터 투입한 돈과 물건값을 입력받는다.
money = int(input("투입한 돈: "))
price = int(input("물건값: "))

change = money - price   # 거스름돈 계산
coin500s = change // 500 # 500원 동전 개수 계산
change = change % 500    # 500원 동전을 뺀 거스름돈 계산
coin100s = change // 100 # 100원 동전 개수 계산

print("500원 동전의 개수:", coin500s)
print("100원 동전의 개수:", coin100s)
