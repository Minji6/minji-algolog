def solution(arr, k):
    answer = []
    data = set()  # 이미 본 숫자 기록용

    for i in arr:
        if i not in data:   # 처음 보는 수라면
            answer.append(i)
            data.add(i)
        if len(answer) == k:  # k개 채우면 바로 종료
            break

    # k개 못 채웠으면 -1로 나머지 채우기
    answer.extend([-1] * (k - len(answer)))

    return answer