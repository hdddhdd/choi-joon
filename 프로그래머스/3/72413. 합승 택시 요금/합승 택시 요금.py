from queue import PriorityQueue

def dijkstra(start, n, adj):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    
    pq = PriorityQueue()
    pq.put((0, start))
    
    while not pq.empty():
        cost, now = pq.get()
        
        if dist[now] < cost:
            continue
        
        for w, nxt in adj[now]:
            new_cost = cost + w
            
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                pq.put((new_cost, nxt))
    
    return dist


def solution(n, s, a, b, fares):
    adj = [[] for _ in range(n+1)]
    
    # 🔥 양방향 그래프 필수
    for c, d, f in fares:
        adj[c].append((f, d))
        adj[d].append((f, c))
    
    dist_s = dijkstra(s, n, adj)
    dist_a = dijkstra(a, n, adj)
    dist_b = dijkstra(b, n, adj)
    
    answer = float('inf')
    
    for k in range(1, n+1):
        answer = min(answer, dist_s[k] + dist_a[k] + dist_b[k])
    
    return answer