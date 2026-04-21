def solution(n, results):
    answer = 0
    origin = [[False]*(n+1) for i in range (n+1)]
    
    for i in range(len(results)):
        origin[results[i][0]][results[i][1]] = True # 이긴 경우

    fw = origin # 업데이트되는 배열
    for k in range (1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if fw[i][k] and fw[k][j]:
                    fw[i][j] = True
    
    for i in range(1, n+1):
        count = 0
        for j in range(1,n+1):
            if i!=j and (fw[i][j] or fw[j][i]): # 2번 기준으로 3번에 대해 진 정보가 있다해도 3번은 2번을 이김. 암튼 순서는 정할 수 있음. 정보가 있어서
                count += 1
        
        if count == n-1:
            answer += 1
            
    
    return answer