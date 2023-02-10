from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
  data = list(map(int, input().split()))
  for c in range(n):
    if data[c] == 1:
      house.append((r, c))
    elif data[c] == 2:
      chicken.append((r, c))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
  result = 0
  # 모든 집에 대하여
  for hx, hy in house:
    # 가장 가까운 치킨집을 찾기
    temp = 1e9
    for cx, cy in candidate:
      temp = min(temp, abs(hx - cx) + abs(hy - cy))
    result += temp
  return result

result = 1e9
for candidate in candidates:
  result = min(result, get_sum(candidate))

print(result)

# ----------------------------------------------------------------------
# 내 풀이
from itertools import combinations 

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

home, chicken = [], []
for a in range(n):
    for b in range(n):
        if data[a][b] == 1:
            home.append((a, b))
        elif data[a][b] == 2:
            chicken.append((a, b))

picked_chicken = list(combinations(chicken, m))

result = 1e9
for picked in picked_chicken:
    city_distance = 0
    for h in home:
        distance = 1e9
        for c in picked:
            distance = min(distance, abs(h[0] - c[0]) + abs(h[1] - c[1])) 
        city_distance += distance
    result = min(result, city_distance)

print(result)