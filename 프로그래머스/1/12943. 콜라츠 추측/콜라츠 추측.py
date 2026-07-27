def solution(num):
    cnt = 0
    
    while (num != 1 and cnt < 500):
        if num % 2 == 0:
            num = num // 2
            cnt += 1
            
        elif num % 2 == 1:
            num = num * 3 + 1
            cnt += 1
    
    if num == 1:
        return cnt
    else: 
        return -1