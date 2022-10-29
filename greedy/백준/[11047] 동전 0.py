import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.reverse()

result = 0
for i in data:
    result += k // i
    k %= i
    if k == 0:
        break
            
print(result)