def solution(myString, pat):
    answer = myString.replace("A", "temp").replace("B", "A").replace("temp", "B")
    return int(pat in answer)