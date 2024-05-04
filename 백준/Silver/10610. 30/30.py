import sys
from collections import Counter 

n = int(sys.stdin.readline().strip())
nList = list(map(int,str(n)))

nList.sort(reverse = True)
nCounter = Counter(nList) # 카운터로 nlist 넣넣 
nListMax = int(''.join(map(str,nList)))

# 마지막에 0이 없으면 우선 30의 배수가 아니므로 바로 -1 출력
if nList[-1] != 0:
    print(-1)
elif nListMax%30 == 0:
    print(nListMax)
else :
    if sum(nList) % 3 != 0:
        print(-1)
    else: 
        result = -1
        # 최대 나올 수 있는 30의 배수로 부터 출발
        n30Count = (nListMax//30)*30
        n30List = list(map(int,str(n30Count)))
        n30Counter = nCounter(n30List)
        while nListMax > 0 :
            if len(nList) != len(n30List):
                break
    
            
            for n30 in n30List:
                if n30Counter[n30] != nCounter[n30] :
                    n30Count -=30
                    n30List = list(map(int,str(n30Count)))
                    n30Counter = nCounter(n30List)
                    break # for break
                    
            # 와일 브레이크ㄹ
            result = n30Count 
            break
        

        print(result)

