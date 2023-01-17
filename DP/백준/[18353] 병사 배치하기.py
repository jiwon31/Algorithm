# dp[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

dp = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

# 열외시켜야 하는 병사의 최소 수 
print(n - max(dp))
