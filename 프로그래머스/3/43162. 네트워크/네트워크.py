def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for j in range(n):
                        if not visited[j] and computers[node][j]==1:
                            stack.append(j)
            count += 1
    
    
    print(count)
    return count