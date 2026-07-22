def solution(x):
    sum = 0
    temp = x
    
    while temp != 0:
        digit = temp % 10
        sum += digit
        temp = temp // 10
    
    if x % sum == 0:
        return True
    else:
        return False