def solution(picture, k):
    answer = []
    
    for row in picture:
        new_row = ''.join(c * k for c in row)
        answer.extend([new_row] * k)
    
    return answer