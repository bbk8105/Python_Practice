x = int(input("정수를 입력하시오(1000의 자리까지만): "))

t = x // 1000                # 천의 자리
h = (x % 1000) // 100        # 백의 자리
ten = (x % 1000) % 100 // 10 # 십의 자리
o = x % 10                   # 1의 자리

sum = t + h + ten + o # 자리수의 합

print("자리수의 합:", sum)
