import sys
sys.setrecursionlimit(10**6)

n , m = map(int,sys.stdin.readline().split())
tList=[]
minTree = [0] * (n*4)
maxTree = [0] * (n*4)

for _ in range(n) :
    tList.append(int(sys.stdin.readline().strip()))


def minBuild(node, start ,end ):
    if start == end :
        minTree[node] = tList[start]
    else :
    # 세팅
        mid = (start + end ) //2
    
        #왼쪽
        minBuild(node*2 , start , mid)
        #오른쪽
        minBuild(node*2+1 , mid+1 ,end)
        minTree[node] = min( minTree[node*2] , minTree[node*2 +1])

def maxBuild(node, start ,end ):
    if start == end :
        maxTree[node] = tList[start]
    else :
    # 세티잉
        mid = (start + end ) //2
        # 왼쪽
        maxBuild(node*2 , start , mid)
        #오른쪽
        maxBuild(node*2+1 , mid+1 ,end)
        maxTree[node] = max( maxTree[node*2] , maxTree[node*2 +1])

##### 최대 최소 세그먼트 트리 세팅#########
minBuild(1,0,n-1)
maxBuild(1,0,n-1)

# 최소값에서 검색 ㄱㄱ
def minQuery(node,start , end , left, rigth ) :

    if rigth<start or end < left :
        return float('inf')
    if left<=start and end <=rigth :
        return minTree[node]
    else : 
        mid = (start+ end ) // 2
        leftNode = minQuery(node*2 ,start ,mid,left,rigth )
        rigthNode = minQuery(node*2+1 , mid+1,end,left,rigth)
        return(min(leftNode,rigthNode))
# 최대값에서 검색 ㄱㄱ
def maxQuery(node,start , end , left, rigth ) :
    # 범위 밖일때ㅇ
    if rigth<start or end < left :
        return -float('inf')
    # start과 end가 범위 안에 있을때  
    if left<=start and end <=rigth :
        return maxTree[node]
    else : 
        mid = (start+ end ) // 2
        leftNode = maxQuery(node*2 ,start ,mid,left,rigth )
        rigthNode = maxQuery(node*2+1 , mid+1,end,left,rigth)
        return(max(leftNode,rigthNode))


#####query########
for a in range(m) : 
    x, y =  map(int,sys.stdin.readline().split())
    minValue = minQuery(1,0,n-1 , x-1, y-1)
    #print(minValue)
    maxValue = maxQuery(1,0,n-1 , x-1, y-1)
    print(minValue,maxValue)

