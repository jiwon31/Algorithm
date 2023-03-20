from itertools import combinations

n = int(input())
board = []
teachers = [] # 선생님 위치 정보
spaces = [] # 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시 진행 (상, 하, 좌, 우)
def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False
    
# 장애물 설치 이후, 학생이 감지되는지 확인
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

result = False

for data in combinations(spaces, 3):
    # 장애물 설치
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        result = True
        break
    # 설치된 장애물 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if result:
    print('YES')
else:
    print('NO')

# -------------------------------------------------------
# DFS
n = int(input())
graph = []
teachers = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def watch(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return True
            nx += dx[i]
            ny += dy[i]
    return False

check = False
def dfs(count):
    global check
    if count == 3:
        for i, j in teachers:
            if watch(i, j):
                return
        check = True
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                dfs(count)
                graph[i][j] = 'X'
                count -= 1

dfs(0)
if check:
    print('YES')
else:
    print('NO')

# -----------------------------------------------------
# combinations
from itertools import combinations

n = int(input())
graph = []
empty_space = []
teachers = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'X':
            empty_space.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_student(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != "O":
            if graph[nx][ny] == "S":
                return True
            nx += dx[i]
            ny += dy[i]
    return False

result = False
obstacles = list(combinations(empty_space, 3))
for obstacle in obstacles:
    count = 0
    for x, y in obstacle:
        graph[x][y] = 'O'
    for i, j in teachers:
        if not check_student(i, j):
            count += 1
    if count == len(teachers):
        result = True
        break
    for x, y in obstacle:
        graph[x][y] = 'X'

if result:
    print('YES')
else:
    print('NO')