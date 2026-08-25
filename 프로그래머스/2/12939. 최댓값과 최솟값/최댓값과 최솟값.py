def solution(s):
    new_s = s.split()
    num_list = list(map(int, new_s))
    
    max_num = max(num_list)
    min_num = min(num_list)
    
    return f"{min_num} {max_num}"
    
    