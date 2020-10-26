import time

fseconds = time.time()

h = (fseconds / 3600) % 24
m = (fseconds / 60) % 60

print("현재 시간(영국 그리니치 시각):", int(h), "시", int(m), "분")
