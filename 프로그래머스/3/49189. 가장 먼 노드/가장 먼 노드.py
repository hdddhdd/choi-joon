from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # print(graph)
    
    dist = [-1] * (n+1)
    dist[1] = 0 # 시작노드 거리는 0으로 고정
    
    q = deque()
    q.append(1) # 시작 노드 넣기
    
    while q:
        # q가 빌 때 까지 (= 더이상 처리할 도착 노드가 없을 때까지)
        # dist 배열 쭉 업데이트 (각각의 최단 거리를 구하면 나오기)
        now = q.popleft()
        
        for next in graph[now]: #now에서 갈 수 있는 next node 탐색
            if (dist[next] == -1): # 탐색되지 않은 노드
                q.append(next)
                dist[next] = dist[now] + 1
    
    max_dist = max(dist)
    cnt = 0
    for d in dist:
        if d == max_dist:
            cnt = cnt + 1
    
    answer = cnt
    return answer