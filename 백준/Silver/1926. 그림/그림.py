from collections import deque
       
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    visited[x][y] = True
    area = 1
    # 상하좌우
    dx = [-1,+1,0 ,0]
    dy = [0,0,-1, +1]

    while queue:
      cx, cy = queue.popleft()
      for i in range(4):
         nx = cx + dx[i]
         ny = cy + dy[i]

         if 0<= nx < n and 0 <= ny <m:
            if not visited[nx][ny] and paper[nx][ny]==1:
               visited[nx][ny]=True
               queue.append((nx,ny))
               area+=1
              
    return area


n, m = map(int, input().split())
paper = []

for _ in range(n):
    paper.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n) ]
# print(visited)

num_paints = 0
max_area = 0
for i in range(n):
  for j in range(m):
    if paper[i][j]==1 and visited[i][j]==False:
      # 방문안했지만 그림이 있는 노드
      cur_area = 0
      cur_area = bfs(i,j)
      if cur_area > 0:
        num_paints+=1
      if max_area < cur_area:
        max_area = cur_area
        
print(num_paints)
print(max_area)

       