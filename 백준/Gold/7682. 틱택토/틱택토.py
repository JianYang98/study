import sys
#sys.stdin=open("input.txt" ,"r")

# 문제 요약 : 주어진 케이스가 틱택토 게임 가능한거야?
# 반드시 첫번째가 X를 놓고 두번째 사람이 O를 놓는다.
# -> 여기서 유추 가능한것이 X의 최대 수는 5 , O의 최대수는 4 개이다.
# - O의 갯수가 X보다 많을 수 없다.
# 유효 케이스
# 1. X 가 이긴다. -> X의 갯수가 많거다  같다 ? .
# 2. O가 이긴다. -> X와 갯수가 같다.
# 3 . 비긴다. -> 바둑판 가득가득쓰 (X가 O보다 더 많아.)

# 3칸 잇기 성공하면 바로 끝나서 (둘다 이기는 케이스는 없어)
# 테스트 케이스를 보고 유추해내는거 진짜 hell..


def makeFan(n) :
    return  [   [n[x],n[x+1],n[x+2]]   for x in range(0,7,3)  ]
def counting(n ,str ) :
    return n.count(str)

def fanVaild(tList ,countX ,countO ):
    # x와 o의 갯수가 유효한지 판별 ( X는 최대 5개 , O는 최대 4)
    if countX >6 or countO >5 or countO >  countX  or countX > countO + 1:
        print("invalid")
        return

    # 여기서 부터 누가누가 이겼나  유효성 체크
    oWin = False
    xWin = False

    for i in range(3):
        # 가로
        if tList[i][0] == tList[i][1] == tList[i][2] == 'X':
            xWin =True
        if tList[i][0] == tList[i][1] == tList[i][2] == 'O':
            oWin =True

        #세로
        if tList[0][i] == tList[1][i] == tList[2][i] == 'X':
            xWin =True
        if tList[0][i] == tList[1][i] == tList[2][i] == 'O':
            oWin =True
    # 대각대각
    if tList[0][0] == tList[1][1] == tList[2][2] == 'X' or tList[0][2] == tList[1][1] == tList[2][0] == 'X':
        xWin = True
    if tList[0][0] == tList[1][1] == tList[2][2] == 'O' or tList[0][2] == tList[1][1] == tList[2][0] == 'O':
        oWin = True

    # 둘다 승리하면 invalid
    if xWin and oWin:
        print("invalid")
        return

    # X가 이겼을 때
    if xWin:
        if countX == countO + 1:
            print("valid")
        else:
            print("invalid")
        return

    # O가 이겼을 때
    if oWin:
        if countX == countO:
            print("valid")
        else:
            print("invalid")
        return

    # 아무도 승리하지 않았을 때
    if not xWin and not oWin:
        if countX == 5 and countO == 4:  # 가득 찼을 때
            print("valid")
        elif countX + countO < 9:  # 아직 빈 칸이 있을 때
            print("invalid")
        else:
            print("valid")
        return

    # 위 모든 조건에 걸리지 않는 경우 invalid
    print("invalid")



if __name__=="__main__":
    while True:
        n = sys.stdin.readline().rstrip()

        # 입력된 문자열이 end 면 break
        if n in 'end' :
            break
        # 카운트 세기
        countX = counting(n, 'X')
        countO = counting(n, 'O')

       # print(countX)
       # print(countO)

        # 3x3 만들기
        tList =makeFan(n)

        # 유효성 검사
        fanVaild(tList ,countX ,countO )

