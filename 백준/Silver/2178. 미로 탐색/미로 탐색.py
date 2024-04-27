import sys
from collections import deque


def BFS():
    bqueue = deque([(0, 0)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while bqueue:
        by, bx = bqueue.popleft()
        if n == by and m == bx:
            print(miro[by][bx])
            break
        for i in range(4):
            fy = by + dy[i]
            fx = bx + dx[i]
            if 0 <= fy < n + 1 and 0 <= fx < m + 1:
                if miro[fy][fx] == 1:
                    miro[fy][fx] = miro[by][bx] + 1
                    bqueue.append((fy, fx))

if __name__ == "__main__" :

    n, m = map(int , sys.stdin.readline().split())
    
    miro= []
    
    for _ in range(n) :
        miro.append( list(map(int,sys.stdin.readline().strip())))
    
    n -=1
    m -=1
    
    BFS()







