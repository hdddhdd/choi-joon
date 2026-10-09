def solution(sizes):
    answer = 0
    # 정렬
    maxw = 0
    maxh = 0
    for i in range(len(sizes)): 
        if (sizes[i][0] < sizes[i][1]):
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
        
        if (sizes[i][0] > maxw):
            maxw = sizes[i][0]
        if (sizes[i][1] > maxh):
            maxh = sizes[i][1]

    answer = maxw * maxh
    
    return answer