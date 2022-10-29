n = int(input())
data = list(map(int, input().split()))
data.sort()

time = 0
result = 0
for i in data:
    time += i
    result += time
    
print(result)

# 다른 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
for i in range(1, n + 1):
  result += sum(data[:i])

print(result)