from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1]*(n+1)
    dist[1] = 0

    q = deque()
    q.append(1)
    
    count = 0
    while  q:
        now = q.popleft()
        
        for next in graph[now]:
            # print(next)
            if dist[next]==-1:
                q.append(next)
                dist[next]=dist[now]+1
    
    # print(dist)
    max_dist = max(dist)
    for d in dist:
        if d == max_dist:
            count+=1
    
    
    return count