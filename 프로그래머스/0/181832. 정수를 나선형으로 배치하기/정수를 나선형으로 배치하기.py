def solution(n):
    answer = [[0] * n for _ in range(n)]
    dr = [0, 1, 0, -1] # 우, 하, 좌, 상
    dc = [1, 0, -1, 0]
    
    r, c = 0, 0
    d = 0
    num = 1
    
    for num in range(1, n*n + 1):
        answer[r][c] = num
        num += 1
        
        nr = r + dr[d]
        nc = c + dc[d]
        
        if nr < 0 or nr >= n or nc < 0 or nc >= n or answer[nr][nc] != 0:
            d = (d+1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
            
        r, c = nr, nc
    return answer
            
        