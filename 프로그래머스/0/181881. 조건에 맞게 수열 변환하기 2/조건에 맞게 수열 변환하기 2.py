def solution(arr):
    answer = 0
    old_arr = arr
    
    while True:
        new_arr = []
        for i in old_arr:
            if i >= 50 and i % 2 == 0:
                i = i // 2
            elif i < 50 and i % 2 != 0:
                i = i * 2 + 1
            new_arr.append(i)
            
        if old_arr == new_arr:
            break
        else:
            old_arr = new_arr
            answer += 1
            
    return answer