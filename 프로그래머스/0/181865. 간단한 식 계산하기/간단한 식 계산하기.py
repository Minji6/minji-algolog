def solution(binomial):
    parts = binomial.split(" ")
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    