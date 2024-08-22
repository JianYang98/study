import sys
#sys.stdin=open("input.txt" ,"r")

# 문제 이해하는 것 자체가 너무 살벌함
# 길이가 N인 밸트가 있고 길이가 2N임
# 벨트가 한칸씩 회전하며 돌아돌아 회전초밥한다.
# 로봇을 올리는 위치(1)에 올릴 수 있고, 내리는 칸 N 번칸에서 칼같이 하차한다.
# 로봇은 내구도가 1 이상 남아있는 곳에만 탑승 가능하다.
# 로봇을 올리려지는 순간 컨베이어 내구도 -1
# 로봇이 한칸씩 이동 가능하다 ( 단 옮기려는 칸 로봇 x, 내구도 0이면 안됨 )
# 로봇이 움직일 수 없으면 가만히 있기 쌉가능
# 내구도가 0인 칸의 개수가 K개 이상이면 과정을 종료한다

# 1 로봇을 올린다.
# - 올리는 곳의 내구도가 0이 아니면 로봇이 탑승한다.
# 올리려는 곳 belt의 내구도가 0아니면 탑승, 아니면 탑승 X

#2 밸트와 로봇이 움직인다.
# 컨버에이터 밸트 싹다 한칸씩 움직인다. ( 뒤에있는거 pop해서 리스트 앞으로 insert()하기)
# 로봇이들로 벨트 처럼 옮겨짐(돌아돌아) - 이건 이동 아님 걍 벨트와 함께 도는거
# 로봇이들 한칸씩 움직임에 따라서 N(내리는곳에 오면 칼같이 내려간다.
# 2- 1 번외 (로봇아 움직일거야?)
#  N-1 칸 부터 다음 칸에 로봇이 없고, 옮기려는 곳의 내구도가 0이 아니면 이동한다.
#  근데 옮겼는데 N이야? 그럼 칼같이 내려가는 거지 뭐 ..(그리고 내구도 -1 한다.)

#3 내구도 체크
# O의 칸의 개수가 K개 이상이면 과정 쌉 종료 break

# break 되어 내려올때의 count 출력하면 될듯

#로봇 탑승 하는 함수
def roobetPut( tList,roobet, n) :
    # 올리는곳의 밸트에 내구도 O 보다 크면 로봇 탑승
    if tList[0] > 0 :
        roobet[0] = True
        tList[0] -= 1
        #print("로보트 올라옴 ")

def roobetTlistRotate(tList, roobet,n):
    # 밸트 이동 tList 뒤값 뽑아서 앞으로 넣기
    tList.insert(0 , tList.pop())
    roobet.insert(0,False)
    
    # 로봇 있냐?
    # 응 이제 없어
    if roobet[n-1] == True:
        roobet[n-1] = False

    # N 칸에 로봇 있는지 확인하고, 없고 내구도 1이상이면 , 뒤에서 로봇땡겨오기(있으면)
    for x in range(n-1,0,-1) :
        # 해당칸에 로봇이 있어?
        if roobet[x] == False and tList[x] > 0 :
            if roobet[x-1] == True :
                roobet[x] = True
                roobet[x-1] = False
                tList[x] -= 1
                if x == n-1 :
                    roobet[x] = False
    roobet.pop()
def check(tList) :
    cnt = 0
    for t in tList:
        if t == 0 :
            cnt+=1
    return cnt





if __name__=="__main__":
    n , k = map(int ,sys.stdin.readline().split())
    tList = list(map(int ,sys.stdin.readline().split()))

    roobet = [False]*n

    count = 0
    while True :
        count +=1
        #1. 밸트와 로봇 둘다 이동이동
        roobetTlistRotate(tList, roobet,n)

        #2. 응 로봇 탑승
        roobetPut(tList, roobet,n)

        #3 내구도 0인 밸트 확인
        if check(tList ) >= k :
            break

    print(count)