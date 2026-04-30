def solution(arr):
    stk = []
    i = 0
    
    for i in range(len(arr)):
        if stk == []:
            stk.append(arr[i])
            i += 1
        elif stk != [] and stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1
            
    if stk == []:
        return [-1]
    
    return stk