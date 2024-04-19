import sys

n = int(sys.stdin.readline().strip())
nList = sorted(list(map(int,sys.stdin.readline().split()))) # O(N log N)
m = int(sys.stdin.readline().strip())
mList = list(map(int,sys.stdin.readline().split()))

def binary(element, min , max ) :
    mid = (min+ max) //2 
    if min > max :        
        return 0 
    if mid >=n:
        return 0
    if element == nList[mid]:
        return 1
    if element > nList[mid]:
        return binary(element,mid+1, max )
    else :
        return  binary(element,min, mid-1 )

for y in mList :
    print(binary(y,0,n-1)  )