from collections import deque

n, k = map(int, input().split())
graph = []
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    # 해당 위치에 바이러스가 존재하는 경우
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 위치 X, 위치 Y
            data.append((graph[i][j], 0, i, j))

# 낮은 번호의 바이러스가 먼저 증식하므로 정렬
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
