import sys
from collections import deque

n, m = map(int , sys.stdin.readline().split())

miro= []

for _ in range(n) :
    miro.append( list(map(int,sys.stdin.readline().strip())))

n -=1
m -=1

def BFS ():
    bqueue = deque([(0,0)])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while bqueue :
        by , bx = bqueue.popleft()
        #print(by," ", bx)
        if n == by and m == bx :
            print(miro[by][bx])
            break
        for i in range(4):
            fy = by + dy[i]
            fx = bx + dx[i]
            if 0<=fy<n+1 and 0<=fx< m+1 :
                #print("fy: " , fy , " fx:", fx) 
                if miro[fy][fx] == 1 :
                    miro[fy][fx] = miro[by][bx] + 1 
                    bqueue.append((fy,fx))
    
BFS()   

