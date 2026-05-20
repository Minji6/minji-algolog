def solution(strArr):
    dict = {}
    
    for s in strArr:
        length = len(s)
        if length in dict:
            dict[length] += 1
        else:
            dict[length] = 1
            
    return max(dict.values())
        