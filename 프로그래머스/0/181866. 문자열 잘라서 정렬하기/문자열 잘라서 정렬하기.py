def solution(myString):
    answer = []
    
    for s in myString.split("x"):
        if s != "":
            answer.append(s)
    answer.sort()

    return answer