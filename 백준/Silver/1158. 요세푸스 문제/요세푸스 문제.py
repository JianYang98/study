from collections import deque # 콜랙션에서 dquer 가져옴 

n,k = map(int,input().split() )
result = []
tmp = [x for x in range(1,n+1)]
tmpDeque= deque(tmp)

while tmpDeque:
    tmpDeque.rotate(-(k-1)) # k-1번 회전함 k번째가 첫번째에서 k-1칸차이
    result.append(tmpDeque.popleft()) # 가장left값 pop

print("<" , end="")
for x in range(n) :
    if x == n-1:
        print(result[x],end="")
    else:
        print(result[x],end=", ")
print(">" , end="")