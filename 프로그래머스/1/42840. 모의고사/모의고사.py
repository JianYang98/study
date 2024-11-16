from collections import deque

def solution(answers):
    
    score = [0] *(3+1)
    nlist1 = deque([1, 2, 3, 4, 5])
    nlist2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    nlist3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    for ele in answers:
        n1 = nlist1.popleft()
        n2 = nlist2.popleft()
        n3 = nlist3.popleft()
        nlist1.append(n1)
        nlist2.append(n2)
        nlist3.append(n3)
        
        if n1 == ele :
            score[1] = score[1] +1
        if n2 == ele :
            score[2] = score[2] +1
        if n3 == ele :
            score[3] = score[3]+1
    
    maxScore = max(score)
    answer = []    
    for i in range(1,4):
        if maxScore == score[i] :
            answer.append(i)

    return answer