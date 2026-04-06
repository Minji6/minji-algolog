def solution(num_list):
    mul = 1
    totalSum = 0 
    
    for i in num_list:
        mul *= i
        totalSum = sum(num_list) ** 2
        
    if mul < totalSum:
        return 1
    else: 
        return 0