# [복습필요!] 좌표 2배한다는 아이디어를 못떠올림.
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 좌표 2배
    rectangle = [[x*2, y*2, x2*2, y2*2] for x, y, x2, y2 in rectangle]
    characterX = characterX * 2
    characterY = characterY * 2
    itemX *= 2 
    itemY *= 2
    
    board = [[0]*102 for _ in range(102)]
    
    # 직사각형 채우기 (테두리 포함)
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2+1):
            for j in range (y1, y2+1):
                board[i][j]=1
    # 내부 제거 
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1+1, x2):
            for j in range(y1+1, y2):
                board[i][j] = 0
    
    # BFS
    q = deque()
    q.append((characterX, characterY, 0))
    visited = [[False]*102 for _ in range(102)]
    visited[characterX][characterY] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q: 
        x, y, dist = q.popleft()
        if x == itemX and y == itemY:
            return dist //2
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 102 and 0<= ny <102:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny, dist+1))

    
    return -1