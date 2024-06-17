import sys
sys.setrecursionlimit(10**6)

n , m = map(int, sys.stdin.readline().split())
tList = []
tList = list(map(int, sys.stdin.readline().split()))
sTree = [0]*(n*4)

def build(node, start, end):


    if start == end :
        # 리프 노드면 원소 저장 
        sTree[node] =  tList[start]
        return 
    else: 
        mid = (start + end) // 2 
        # 재귀 ㄱㄱ
    
        # 왼쪽 자식 재귀 ( 왼쪽 자식의 노드는 node*2, 범위는 start ~ mid)
        build(node*2, start , mid)
        #오른쪽 자식의 재귀 (오른쪽 노드는 node+1 , 범위는 mid+1 ~ end 까지다)
        build(node*2+1, mid+1 , end)
        #내부 노드면 두자식의 노드 값 쌉저장ㄴ
        sTree[node] = sTree[node*2] + sTree[node*2 + 1]
    return 
build(1,0,n-1)

# 구간 합 구하기  뺌~~~
# node가 담당하는 구간 [start, end]
#합을 구해야하는 구간 [left,right]
def query(node,start,end,left,right):

    if right<start or end < left :
        return 0
    if left <= start and end <= right:
    # 노드가 지정 범위 안에 있으면 ?
        return sTree[node]

    #노드가 지정된 범위 일부에 있을때는 ? 
    mid = (start + end ) //2
    #왼
    leftChild = query(node*2, start, mid, left, right)
    #오
    rightChild = query(node*2+1, mid+1, end, left, right)
    # 결과 뺩
    return leftChild  +  rightChild

    


for x in range(m) :
    a , b = map(int, sys.stdin.readline().split())
    print(query(1,0,n-1,a-1,b-1))
    







