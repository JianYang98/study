import sys
sys.setrecursionlimit(10**6)

n , m, k = map(int,sys.stdin.readline().split())

# 트리
tree = [0] *(n*4)
tList = []
for _ in range(n) :
    tList.append(int(sys.stdin.readline().strip()))

#기초 공사 build
def build(node,start , end ):
    if start == end :
        tree[node] =tList[start]
    else :
        mid = (start + end ) // 2 
        # d왼쪽노ㅉ
        build(node*2 , start , mid)
        #오른쪽 노드
        build(node*2 +1 , mid+1 ,end)
        tree[node] = tree[node*2] + tree[node*2 + 1]
# query 찾기 찾기
def query(node, start , end , left, right):
    if right<start or end < left :
        return 0
    # start와 end 의 start와 end가 left ,rigth 범위일때 ㄸ
    if left<=start and  end<= right:
        return tree[node]
    
    # 범위가 걸쳐 있을때
    mid  = (start + end ) // 2 
    leftLeaf = query(node*2 , start , mid , left , right)
    rigthLeaf = query(node*2 + 1 , mid +1 , end, left , right)
        #print(mid)
    return leftLeaf + rigthLeaf

# 업뎃업뎃    
def update(node, start , end , index , val ) :
    if start == end :
        tree[node] = val 
        return  
    mid = (start + end ) // 2 
    if start<= index <=mid :
        update(node*2 , start, mid , index , val )
    else : 
        update(node*2+1 , mid+1 , end ,index , val )
    tree[node] = tree[node*2] + tree[node*2 + 1]
        



# 구성구성
build(1,0,n-1)        

for _ in range(m+k ) :
    a,b,c = map(int,sys.stdin.readline().split())
    #print("a,b,c ", a,b,c)
    # 1일떄 update
    if a == 1 :
        update(1,0,n-1,b-1,c)
    # 1이 아닐떄 query로 범위 값 찾기 
    else :
        print(query(1,0,n-1,b-1,c-1))