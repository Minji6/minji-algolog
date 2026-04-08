def solution(l, r):
    answer = []

    for i in range(l, r+1):
        if all(s == '0' or s == '5' for s in str(i)):
            answer.append(i)
    if answer == []:
        return [-1]
    
    return answer