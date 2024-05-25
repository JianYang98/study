import sys

t = int(sys.stdin.readline().strip())
tList = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(t)]

# i번째 원소를 끝으로 하는 수열 구할 거임 
for i in range(t):
    
    # i 번째 원소보다 앞에 있는 모든 원수 구할 거임 
    for j in range(i):
        
        # i 번째 보다  앞에있는 j 일때 dp[i] 값 업뎃침 
        if tList[j] > tList[i]:
            #i까지 왔으려면 어차피 j들을 순회있어야한다. j 모든 경우의 수 +1 ㄱㄱㄱ
            dp[i] = max(dp[i],dp[j]+1)


print(max(dp))