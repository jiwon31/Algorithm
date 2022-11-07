data = list(map(int, input()))
i = len(data) // 2

result1 = sum(data[:i])
result2 = sum(data[i:])
if result1 == result2:
  print('LUCKY')
else:
  print('READY')


# ----- 다른 풀이 -----
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
  summary += int(n[i])

for i in range(length // 2, length):
  summary -= int(n[i])

if summary == 0:
  print('LUCKY')
else:
  print('READY')