def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:
        sliceStr = i[s:s+l]
        sliceStr = int(sliceStr)
        
        if sliceStr > k:
            answer.append(sliceStr)
            
    return answer