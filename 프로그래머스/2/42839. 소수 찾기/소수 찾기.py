from itertools import permutations
def solution(numbers):
    answer = 0
    # 모든 조합 구하기
    tmp = []
    candset = set() # set

    for n in numbers:
        tmp.append(n)
        
    for i in range(1, len(tmp)+1):
        for perm in permutations(tmp, i): # permutations
            candset.add(int(''.join(perm))) # ''.join(perm): 문자열 사이에 넣을 구분자('')로 join
    
    for c in candset:
        if (is_prime(c) == True):
            answer = answer + 1
            
    return answer
    

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
    return True