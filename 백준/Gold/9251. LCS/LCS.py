import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

strI = len(str1)
strJ = len(str2)
#print(strJ)
#print(strI)

# dp 초기화기
dp = [   [0]*(strJ+1) for x in range(strI+1)    ]

#점화식
for i in range(1 ,strI+1 ) :
    for j in range(1 , strJ+1 ) :
        #print(i,j)
        if str1[i-1] == str2[j-1] :
            dp[i][j] = dp[i-1][j-1] +1
        else : 
            dp[i][j] = max( dp[i-1][j] , dp[i][j-1]      )
        

print(dp[strI][strJ])