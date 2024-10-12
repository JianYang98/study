import sys
from collections import deque
sys.setrecursionlimit(10**6)

#sys.stdin = open("input.txt", "r")


def BFS ():
    global n, m
    bqueue  = deque([(0,0)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while bqueue :
        by  , bx = bqueue.popleft()
        #print(by, " ", bx)
        #print(n, " n : m  ", m)
        if n  ==by+1 and m == bx+1 :
            print(nList[by][bx])
            break

        # 큐에서 값 pop()
        for i in range(4):
            fy = by + dy[i]
            fx = bx + dx[i]
            if 0<=fy<n and 0<=fx< m : #상하좌우 탐색 할 좌표 값 범위 체크
                if nList[fy][fx] == 1 :
                    nList[fy][fx] = nList[by][bx] + 1

                    bqueue.append((fy,fx))




if __name__ == "__main__" :
    n , m = map(int, sys.stdin.readline().split())
    nList = []
    for __ in range(n):
        nList.append(list(map(int, sys.stdin.readline().strip())))
    BFS()

