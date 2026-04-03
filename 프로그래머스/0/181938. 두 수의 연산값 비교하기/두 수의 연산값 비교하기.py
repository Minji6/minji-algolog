def solution(a, b):
    
    ab = str(a) + str(b)
    multiply_ab = str(2*a*b)
    
    answer = max(int(ab), int(multiply_ab))
    
    return answer