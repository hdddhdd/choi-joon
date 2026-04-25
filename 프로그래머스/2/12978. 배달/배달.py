import heapq
def solution(N, road, K):
    answer = 0
    # 0번은 다 무시하기
    # 1. adj 배열 2차원 만들기
    adj = [[]*(N+1) for _ in range(N+1)]
    
    for r in road:
        s, e, d = r
        adj[s].append((e,d))
        adj[e].append((s,d))
    # print('adj: ', adj)
    
    # 2. 다익스트라 알고리즘
    dist = [1e9]*(N+1)
    hq = []
    visited = [False] * (N+1)
    
    heapq.heappush(hq, (0, 1))
    visited[1] = True
    dist[1] = 0
    
    while hq:
        tempdist, tempnode = heapq.heappop(hq)

        for adjinfo in adj[tempnode]:
            
            adjnode, adjdist = adjinfo
            
            if not visited[adjnode]:

                if adjdist + tempdist < dist[adjnode]:
                    dist[adjnode] = adjdist + tempdist
                    heapq.heappush(hq, (dist[adjnode], adjnode))
            
    # print(dist)
    count = 0
    for i in range(1, N+1):
        if dist[i] <= K:
            count += 1
    
                
    
    
    
    return count