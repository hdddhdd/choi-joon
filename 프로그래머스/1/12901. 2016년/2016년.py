def solution(a, b):
    answer = ''
    dates = [31,29,31,30,31,30,31,31,30,31,30,31]
    total_dates = 0
    for i in range (1, a+1):
        if a == 1: # 1월일 때
            total_dates = b-1
            break
        else: # 1월 아닐 때
            if i == 1: # 1월은 30일만큼 더함.
                total_dates += 30
            elif i == a: # 해당 월은 그 일수만큼 더함.
                total_dates += b
            else: # 그 외의 월은 전체 날짜만큼 더함.
                total_dates += dates[i-1]
    answer_idx = total_dates % 7
    answer_list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    answer = answer_list[answer_idx]
        
    
    return answer