n = int(input())

dp = []
for _ in range(n):
  dp.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(i + 1):
    # 왼쪽 위에서 내려오는 경우
    if j == 0:
      left_up = 0
    else:
      left_up = dp[i - 1][j - 1]
    # 바로 위에서 내려오는 경우
    if j == i:
      up = 0
    else:
      up = dp[i - 1][j]
    dp[i][j] = dp[i][j] + max(left_up, up)

print(max(dp[n - 1]))
