n, k = map(int, input().split())
result = 0

while n >= k:
  while n % k != 0:
    n -= 1
    result += 1
  n //= k
  result += 1
  
while n > 1:
  n -= 1
  result += 1

print(result)

# ---------------------------------------------
# 내 풀이
n, k = map(int, input().split())
count = 0

while n != 1:
  if n % k == 0:
    n //= k
    count += 1
  else:
    n -= 1
    count += 1

print(count)