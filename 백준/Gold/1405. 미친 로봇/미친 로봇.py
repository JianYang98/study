import sys
#sys.stdin = open("input.txt", "r")


def DFS(n, y, x, r):
    global result, t
    # 이미 방문한 경우 종료
    if gList[y][x]:
        return
    # 남은 이동 횟수가 0이면 확률을 누적
    if n == 0:
        result += r
        return

    # 동, 서, 남, 북 이동 방향 정의
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 현재 위치 방문 표시
    gList[y][x] = True

    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 경계 내에 있고 해당 방향의 확률이 0보다 클 때 탐색
        if 0 <= nx < 2 * t + 1 and 0 <= ny < 2 * t + 1 and na[i] > 0:
            DFS(n - 1, ny, nx, r * na[i] * 0.01)

    # 백트래킹 시 방문 해제
    gList[y][x] = False


if __name__ == "__main__":
    t, e, w, s, n = map(int, sys.stdin.readline().split())
    # 각 방향의 확률 리스트 (동, 서, 남, 북 순서)
    na = [e, w, s, n]
    # 방문 체크 배열 (2t + 1) x (2t + 1) 생성
    gList = [[False] * (2 * t + 1) for _ in range(2 * t + 1)]
    result = 0.0  # 확률의 합 초기화
    # DFS 탐색 시작 (초기 위치는 가운데)
    DFS(t, t, t, 1)
    # 결과 출력
    print(result)#