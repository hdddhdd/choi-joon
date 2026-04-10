from collections import deque
def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((0,0,1))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        
        curx, cury, curdist = q.popleft()
        if curx == n-1 and cury == m-1:
            return curdist
        
        for i in range(4):
            if 0<= curx + dx[i] < n and 0<= cury + dy[i] < m and visited[curx+dx[i]][cury+dy[i]]==False and maps[curx+dx[i]][cury+dy[i]]==1:
                # 이동 가능

                q.append((curx+dx[i], cury+dy[i], curdist+1))
                visited[curx+dx[i]][cury+dy[i]]=True


        
    answer = -1
    return answer