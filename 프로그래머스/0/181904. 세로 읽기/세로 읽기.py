# 이건 [[r],[c]] 형태네
# 가로로 m 글자씩 잘라 r에 넣으면 알아서 c도 되겠군

def solution(my_string, m, c):
    answer = ''
    result = []
    for i in range(0, len(my_string), m):
        result.append(my_string[i:m+i])
        
    for j in range(len(result)):
        answer += result[j][c-1]
        
    return answer