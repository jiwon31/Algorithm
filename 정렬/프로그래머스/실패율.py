# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 내 풀이
def solution(N, stages):
    array = [0] * (N + 1)
    for i in stages:
        if i <= N:
            array[i] += 1

    fail = []    
    length = len(stages)
    for i in range(1, len(array)):
        if length == 0:
            rate = 0
        else:
            rate = array[i] / length
        fail.append((i, rate))
        length -= array[i]
        
    fail.sort(key= lambda x: (-x[1], x[0]))
    
    answer = [i[0] for i in fail]
    return answer

# -----------------------------------------------------------------

def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N + 1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        answer.append((i, fail))
        length -= count
    
    answer = sorted(answer, key= lambda x: x[1], reverse=True)
    
    answer = [i[0] for i in answer]
    return answer
