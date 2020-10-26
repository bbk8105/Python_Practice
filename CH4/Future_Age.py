import time

now = time.time()

thisYear = int(1970 + now // (365*24*3600))

print("올해는 " + str(thisYear) + "년도입니다.")
a = int(input("몇살이신지요?: "))
print("2050년에는 " + str(a + 2050 - thisYear) + "살 이신군요.")
