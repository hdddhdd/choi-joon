def solution(numbers, target):
    answer = 0

    answer = dfs(numbers, target, 0, 0)
    
    return answer

def dfs(numbers, target, idx, total):
    if (idx == len(numbers)):
        # 종료 조건
        # 종료 조건에서 target == total인 경우 -> return 1 / 그렇지 않은 경우 return 0
        if (target == total):
            return 1
        else: 
            return 0
    
    # 종료조건이 아니라면 numbers에서 뽑기
    
    # 다음 실행할 idx+1해주고, total 계속 업데이트
    plus = dfs(numbers, target, idx+1, total+numbers[idx]) #방금 앞에까지 결과에 plus로 끝까지 가고 그 결과를 
    minus = dfs(numbers, target, idx+1, total-numbers[idx])
    
    return plus + minus

