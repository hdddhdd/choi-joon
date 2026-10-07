from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((0,0,1)) #큐에 넣고 빼고 
    
    while q:
        curx, cury, curdist = q.popleft()
        if (curx == n-1 and cury == m-1):
            #종료 조건
            return curdist
        for i in range(4): # 상하좌우
            movex = curx + dx[i]
            movey = cury + dy[i]
            
            if (0<= movex < n and 0<= movey < m and
                visited[movex][movey] == False and
               maps[movex][movey] == 1):
                #이동 가능
                q.append((movex, movey, curdist+1))
                visited[movex][movey] = True
                
    answer = -1
    
    return answer