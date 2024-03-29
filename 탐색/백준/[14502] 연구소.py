n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    # 벽이 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    # 빈 공간에 벽 설치 
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

# --------------------------------------------------------------
# combinations 모듈 사용한 풀이
from itertools import combinations

# ... 중간은 똑같음 ...

empty_space = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            empty_space.append((i, j))

walls = combinations(empty_space, 3)
result = 0
for wall in walls:
    for wx, wy in wall:
        data[wx][wy] = 1
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]        
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                virus(i, j)
    result = max(result, get_score())
    for wx, wy in wall:
        data[wx][wy] = 0

print(result)