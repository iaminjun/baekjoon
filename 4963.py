dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def dfs(x,y):
  if x < 0 or y < 0 or x >= h or y >= w:
    return False
  if mymap[x][y] != 1:
    return False

  mymap[x][y] = 2
  for i in range(8):
    dfs(x + dx[i], y + dy[i])
  return True


while True:
  w, h = map(int, input().split())
  if w == 0 and h ==0:
    break
  mymap = []
  for i in range(h):
    mymap.append(list(map(int,input().split())))


  num_of_island = 0
  for i in range(h):
    for j in range(w):
      if dfs(i,j):
        num_of_island += 1

  print(num_of_island)
       
