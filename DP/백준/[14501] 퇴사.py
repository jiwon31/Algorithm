# dp[i]는 i번째 날부터 마지막 날까지 낼 수 있는 최대 이익

n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
  time = t[i] + i
  # 상담이 기간 안에 끝나는 경우
  if time <= n:
    dp[i] = max(p[i] + dp[time], max_value)
    max_value = dp[i]
  # 기간을 벗어나는 경우  
  else:
    dp[i] = max_value

print(max_value)
