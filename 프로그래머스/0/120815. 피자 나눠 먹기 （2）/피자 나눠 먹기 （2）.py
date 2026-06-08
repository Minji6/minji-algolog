def solution(n):
    lcm = 6
    while lcm % n != 0:
        lcm += 6
    return lcm // 6