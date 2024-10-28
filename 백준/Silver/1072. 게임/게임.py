import sys

x, y = map(int, sys.stdin.readline().split())

result = -1 # 최소 횟수 계산
tmp = 0
z = (y * 100) // x

start = 0
end = 1000000000
mid = 0

while start <= end : 
    mid = (start + end) //2
    # 새로운 승률 계산로
    new = ((y + mid ) * 100)// (x + mid) # 내가 생각못한 부분임 ㅅ
    if new >  z : # 승률이 증가한 경유ㅅ
        
        result = mid
        end = mid -1
    else :
        start = mid +1 
print(result)