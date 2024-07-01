import sys
#from bisect import bisect_left
#from bisect import bisect_right

n = int(sys.stdin.readline().strip())
tList = list(map(int ,  sys.stdin.readline().split()))

dpMax=[1] * n
dpMin= [1] * n

for i in range(n-1):
    # 증가 수열일 경루
    if tList[ i+1 ] >= tList[i] :
        dpMax[i+1] += dpMax[i]
    if tList[ i+1 ] <= tList[i] :
        dpMin[i+1] += dpMin[i]    
     
#print(",max(dpMin) " ,max(dpMin))
#print(len(dpMin))
#print("dpMax " , max(dpMax))
#print(len(dpMax))
print( max(  max(dpMin) , max(dpMax)  )    )


