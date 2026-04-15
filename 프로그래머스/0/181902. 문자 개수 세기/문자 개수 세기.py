def solution(my_string):
    answer = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz'
    
    for alphabet in alphabets:
        answer.append(my_string.count(alphabet))
    
    return answer