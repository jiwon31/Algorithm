n = int(input())

d = [0] * n
d[0] = 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

for j in range(1, n):
  d[j] = min(next2, next3, next5)
  if d[j] == next2:
    i2 += 1
    next2 = d[i2] * 2
  if d[j] == next3:
    i3 += 1
    next3 = d[i3] * 3
  if d[j] == next5:
    i5 += 1
    next5 = d[i5] * 5

print(d[n - 1])