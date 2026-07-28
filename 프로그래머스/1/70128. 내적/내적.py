def solution(a, b):
    sum = 0
    for x, y in zip(a, b):
        mul = x * y
        sum += mul
    return sum