def solution(num_list):
    sum = 0
    mul = 1
    
    for i in range(len(num_list)):
        sum += num_list[i]
        mul *= num_list[i]
    
    if len(num_list) >= 11:
        return sum
    else:
        return mul
    