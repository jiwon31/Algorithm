n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()

result = 0
for i in range(n):
    max_value = b.pop(b.index(max(b)))
    result += a[i] * max_value

print(result)