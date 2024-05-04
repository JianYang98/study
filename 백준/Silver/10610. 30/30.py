import sys
from collections import Counter 

n = int(sys.stdin.readline().strip())
nList = list(map(int,str(n)))

nList.sort(reverse = True)

nListMax = int(''.join(map(str,nList)))

# 마지막에 0이 없으면 우선 30의 배수가 아니므로 바로 -1 출력
if nList[-1] != 0:
    print(-1)
elif  sum(nList) % 3 != 0:
    print(-1)  
elif nListMax%30 == 0:
    print(nListMax)
else :
    print(-1)