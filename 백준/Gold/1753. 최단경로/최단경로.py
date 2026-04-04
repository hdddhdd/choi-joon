import sys
input = sys.stdin.readline
from queue import PriorityQueue
V, E = map(int, input().split())
K = int(input())-1
adj = [[] for _ in range(V)] 
for i in range(E):
  u,v,w = map(int, input().split())
  adj[u-1].append((w, v-1)) # (거리, 노드) 형태로 저장

dist = [1e9]*V
dist[K]=0


pq = PriorityQueue()
pq.put((0, K))

while not pq.empty():
  d, u = pq.get()

  if dist[u] < d:
    continue 

  for w, v in adj[u]:
    if dist[v] > dist[u] + w:
      dist[v] = dist[u]+w
      pq.put((dist[v], v))

for d in dist:
  if d==1e9:
    print("INF")
  else:
    print(d)
