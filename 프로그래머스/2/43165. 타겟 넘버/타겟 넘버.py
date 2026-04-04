def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for leave in leaves:
            tmp.append(leave + num)
            tmp.append(leave - num)
        leaves = tmp
            
    for leave in leaves:
        if leave == target:
            answer += 1
    return answer