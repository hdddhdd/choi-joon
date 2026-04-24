from collections import deque

def can_change(a,b):
    count=0
    for i in range(len(a)):
        if a[i] == b[i]:
            count+=1
    if count == len(a)-1:
        return 1
    else:
        return 0
    
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0)) # word, step
    step = 0
    
    visited = [False] * len(words)
    
    while queue:
        word, step = queue.popleft()
        if word == target:
            return step
        
        for i in range(len(words)):
            
            if not visited[i] and can_change(word, words[i]):
                
                print('current word: ', words[i])
                visited[i] = True
                step += 1
                queue.append((words[i], step))
                
    
    # print('step: ', step)
    
    return 0