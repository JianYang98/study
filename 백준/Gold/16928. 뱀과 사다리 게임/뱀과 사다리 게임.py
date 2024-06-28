
import sys
from collections import deque

n , m = map(int,sys.stdin.readline().split())
tList = [ x for x in range(0,101)]
sa = {}
snake ={}
q = []
for _ in range(n):
    
    a , b = map(int,sys.stdin.readline().split())
    sa[a] = b
for _ in range(m):
    a , b = map(int,sys.stdin.readline().split())
    snake[a] = b

def BFS(a) :
    board = [0] * 101  # 1부터 100까지의 칸을 표현
    visited =[False] * 101
    q = deque([1])
    cnt = 0

    while q:
        a   = q.popleft()
        
  
        if a  == 100 :
             
    
            return board[a]
    
    
        for dice  in range(1,7) :
            nextNode = (a )+  dice 
            if nextNode <= 100  :
                # 값이 사다리에 있어 ?ㅇ
                if nextNode in sa :
                    nextNode = sa[nextNode]
                # 값이 t뱀에 있어? 
                elif nextNode in snake :
                    nextNode = snake[nextNode]
                else:
                    nextNode = nextNode 
                if   visited[nextNode] == False :
                    visited[nextNode] = True 
                    q.append(nextNode)
                    board[nextNode] = board[a] +1
            
                
    

cnt = BFS(1)
print(cnt)
    
    

    
    
    