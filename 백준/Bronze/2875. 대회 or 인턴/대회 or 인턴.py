import sys
from collections import deque

n , m ,k = map(int,sys.stdin.readline().split())
team = 0
while n+m > k :
    
    if n -2 >=0 and m-1 >=0 and (n-2 + m-1) >= k:
        n-=2
        m-=1
        team+=1

    else:
        break
        
print(team)
    
