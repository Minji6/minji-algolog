# 결국 이 보드 안에서 k값을 만족하거나 그것보다 더 작은 값들의 합을 구하라

def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                answer += board[i][j]
    return answer