def solution(s):
    answer = True
    check_len = False
    check_num = False
    
    if (len(s)==4 or len(s)==6):
        check_len = True
    if s.isdigit():
        check_num = True
    answer = check_len and check_num  
    
    return answer