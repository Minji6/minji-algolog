def solution(numbers, n):
    answer = 0
    sum = 0
    
    for i in range(len(numbers)):
        sum += numbers[i]
        
        if sum > n:
            return sum