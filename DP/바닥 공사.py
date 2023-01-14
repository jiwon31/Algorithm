# d[i]는 가로가 i일 때 바닥을 채우는 경우의 수
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
  d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])
