# https://school.programmers.co.kr/learn/courses/30/lessons/42889

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

# -----------------------------------------------------------------
# 내 풀이
def solution(N, stages):
    answer = []
    failure_rate = []

    for i in range(1, N + 1):
        count = 0
        not_clear = 0
        rate = 0
        for stage in stages:
            if i == stage:
                not_clear += 1
            if stage >= i:
                count += 1
        if count == 0:
            rate = 0
        else:
            rate = not_clear / count
        failure_rate.append((rate ,i))
    
    failure_rate.sort(key=lambda x: -x[0])
    for i in failure_rate:
        answer.append(i[1])
        
    return answer