import sys
from collections import Counter

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    team = list(map(int,sys.stdin.readline().split()))
    counter = Counter(team)
    score= {}

    rank =1
    for i in range(n):
        if counter[team[i]] == 6 : # 명이고고
            if  team[i] in score:
                score[team[i]].append(rank) 
            else : 
                score[team[i]] = [rank]
            rank +=1
    #print(score)
    print(sorted(score, key = lambda x:(sum(score[x][0:4]), score[x][4]))[0])



