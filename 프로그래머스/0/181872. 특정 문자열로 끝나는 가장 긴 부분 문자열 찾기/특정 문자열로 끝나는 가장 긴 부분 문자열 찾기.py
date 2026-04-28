def solution(myString, pat):
    answer = ''
    
    rindex = myString.rfind(pat)
    answer += myString[:rindex+len(pat)]
    
    return answer