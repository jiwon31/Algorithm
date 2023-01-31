n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
for x in data:
  array[x] += 1

result = 0
for i in range(1, m + 1):
  n -= array[i]
  result += array[i] * n

print(result)

# -----------------------------------------------
# 내 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * (m + 1)
for i in data:
  array[i] += 1

result = 0
for i in range(1, m + 1):
# A가 고른 공의 개수 * A가 고른 공의 개수 제외한 볼링공의 개수
  count = array[i] * sum(array[i + 1:]) 
  result += count

print(result)