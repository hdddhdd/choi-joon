def solution(N, number):
    answer = 0
    if N==number:
        return 1
    dp = [set() for _ in range(9)] # 0~8
    
    for i in range(1,9): # 1~8
        # 이어 붙이기
        dp[i].add(int(str(N)*i))
        
        
        for j in range(1,i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y!=0:
                        dp[i].add(x//y)

        if number in dp[i]:
            return i
    return -1
                    
                    
    
    # return answer