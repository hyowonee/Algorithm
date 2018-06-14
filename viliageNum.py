def dfs():
  visit[v] = 1
  for i in range(mapSize):
    for j in range(mapSize):
      if viliage[i][j] == 1 and not visit[i]:
        dfs()
mapSize = int(input())
viliage = [[0]* mapSize for i in range(mapSize)]
visit = [0] * mapSize 

for i in range(mapSize):
  viliage[i] = list(map(int, input()))
  dfs()

dx = [1, 0, -1, 0] // ?
dy = [0, 1, 0, -1] // ??

size = int(input())
arr = []

def dfs(x, y): // dfs
  arr[y][x] = 0
  count = 1
  for i in range(0, 4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= size or ny >= size:
        continue
    if arr[ny][nx] == 1:
      count += dfs(nx, ny)
  return count

for _ in range(size):
  arr.append(list(map(int, input())))

results = []
for i in range(size):
  for j in range(size):
    if arr[i][j] == 1:
      results.append(dfs(j, i))

print(len(results))
results.sort()
for result in results:
  print(result)