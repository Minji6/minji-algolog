def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(my_strings)):
        my_strings[i]
        s = parts[i][0]
        e = parts[i][1]
        
        answer += my_strings[i][s:e+1]
    return answer