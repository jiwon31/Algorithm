n = int(input())
data = []

for _ in range(n):
    start, end = map(int, input().split())
    data.append([start, end])

# 끝나는 시간의 오름차순으로 정렬 후, 시작하는 시간의 오름차순으로 정렬
data.sort(key = lambda x: (x[1], x[0]))

result = 0
end_time = 0
for i in data:
    if i[0] >= end_time:
        result += 1
        end_time = i[1]
        
print(result)