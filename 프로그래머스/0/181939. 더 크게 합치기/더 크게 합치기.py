def solution(a, b):
    str_a = str(a)
    str_b = str(b)
    
    ab = str_a + str_b
    ba = str_b + str_a
    
    if ab > ba or ab == ba:
        return int(ab)
    else:
        return int(ba)