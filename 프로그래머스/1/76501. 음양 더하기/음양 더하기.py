def solution(absolutes, signs):
    sum = 0
    for num, sign in zip(absolutes, signs):
        if sign == True:
            sum += num
        else:
            sum -= num
    return sum