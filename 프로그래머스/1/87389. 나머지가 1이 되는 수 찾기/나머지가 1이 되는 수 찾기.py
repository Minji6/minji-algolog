def solution(n):
    for x in range(1, n+1):
        if x > n:
            return n
        else:
            if n % x == 1:
                return x