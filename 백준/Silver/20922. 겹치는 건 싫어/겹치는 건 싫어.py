import sys
from collections import defaultdict

n , k = map(int, sys.stdin.readline().split())
tList = list( map(int, sys.stdin.readline().split()))

tDict = defaultdict(int)

start =0
cnt = 0 
maxLen = 0 
# end 값이 n보다 크면 break 끝ㄲ
for end in range(n) :
    tDict[tList[end]] +=1
    
    # 슬라이딩 윈도우 , 쌉 시작
    # 딕셔너리에 있는 값이 k보다 크면?
    # while을 돌면서 start의 값을 갱신한다.
    # start의 범위 값이 올라다니 당연히 tDict[start] -=1 이된다.
    while tDict[tList[end]] > k :
        tDict[tList[start]] -=1
        start+=1

    # 길이 구하기 
    maxLen = max(maxLen , end - start +1 )
        
print(maxLen)