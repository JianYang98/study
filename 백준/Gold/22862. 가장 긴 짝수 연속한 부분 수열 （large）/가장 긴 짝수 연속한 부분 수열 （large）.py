import sys

n , k = map(int, sys.stdin.readline().split())
tList = list(map(int, sys.stdin.readline().split()))

end = 0 # 끝 포인터
result = 0 # 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이(출력값)
tmp = 0 # 현재 짝수 부분 수열의 길이
count = 0 # 지우려는 홀수 카운트

# start를 N 까지 계속 증가시키며 반복
for start in range(n):
    
    # end를 가능한 만큼 이동
    while (count <= k and end < n):     
        
        if tList[end] % 2 == 1: # 홀수
            count += 1 # 홀수 일때 지울 수 upup
        else: # 짝수
            tmp += 1 # 짝수 일때 수열 길이 upup 
        end += 1 # 끝 점 이동
        
        if start == 0 and end == n:  # 시작점이 0이여? end 가 끝이여 ? 
            result = tmp
            break
    # 홀수가 k+1 개 일때 , 지금까지의 짝수갯수가 최대여     
    if count == k+1 :
        result = max(tmp, result)
        
    if tList[start] %2 == 1: # 시작점이 홀수
        count -= 1
    else: # 시작점이 짝수
        tmp -= 1
print(result)
