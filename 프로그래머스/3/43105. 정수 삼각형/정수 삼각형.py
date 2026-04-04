def solution(t):
    answer = 0
    
    n = len(t[len(t)-1])
    dp = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1):
            if i==0 and j==0:
                dp[i][j] = t[0][0]
            else:
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + t[i][j]
                elif j==0:
                    dp[i][j] = dp[i-1][j] + t[i][j]
                elif j==i:
                    dp[i][j] = dp[i-1][j-1] + t[i][j]
    
    print(max(dp[n-1]))
    answer = max(dp[n-1])
    
    return answer