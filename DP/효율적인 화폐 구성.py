# d[i]는 금액 i를 만들 수 있는 최소한의 화폐 개수

n, m = map(int, input().split())
array = []
for _ in range(n):
  array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] != 10001:
  print(d[m])
else:
  print(-1)
