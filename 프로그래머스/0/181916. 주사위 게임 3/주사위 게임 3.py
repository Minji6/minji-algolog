from collections import Counter

def solution(a, b, c, d):
    cnt = Counter([a,b,c,d])
    counts = list(cnt.values())
    counts.sort(reverse=True)
    p = None
    q = None
    
    if counts == [4]:
        p = list(cnt.keys())[0]
        answer = 1111 * p
        
    elif counts == [3,1]:
        for key, value in cnt.items():
            if value == 3:
                p = key
            if value == 1:
                q = key
        answer = (10 * p + q) ** 2
    
    elif counts == [2,2]:
        for key, value in cnt.items():
            if value == 2 and p == None:
                p = key
            elif value == 2:
                q = key
        answer = (p+q) * abs(p-q)

    elif counts == [2,1,1]:
        for key, value in cnt.items():
            if value == 2 and p == None:
                p = key
            elif value == 1 and q == None:
                q = key
            elif value == 1:
                r = key
        answer = q * r
                
    else: answer = min(a,b,c,d)
    
        
    return answer