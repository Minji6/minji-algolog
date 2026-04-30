def solution(arr, k):
    answer = []
    
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break
    
    if len(answer) < k:
        answer += (k - len(answer)) * [-1]
    
    return answer