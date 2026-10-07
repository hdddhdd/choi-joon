def solution(s):
    answer = ''
    mylist = list(map(int, s.split()))
    answer = str(min(mylist)) + " " + str(max(mylist))
    # print(answer)
    return answer