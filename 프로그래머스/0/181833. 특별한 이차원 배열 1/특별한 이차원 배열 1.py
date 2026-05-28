def solution(n):
    answer = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(i == j))
        answer.append(row)
    return answer