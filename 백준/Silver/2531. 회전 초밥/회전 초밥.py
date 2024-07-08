import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input().rstrip()) for _ in range(n)]

current_sushi = [0] * (d + 1)  # 초밥의 종류를 카운트하기 위한 리스트
current_count = 0  # 현재 윈도우 내의 초밥 종류의 수

# 초기 윈도우 설정
for i in range(k):
    if current_sushi[sushi[i]] == 0:
        current_count += 1
    current_sushi[sushi[i]] += 1

# 쿠폰 초밥 추가
answer = current_count
if current_sushi[c] == 0:
    answer += 1

# 슬라이딩 윈도우
for i in range(1, n):
    # 윈도우의 왼쪽 끝 초밥 제거
    left_sushi = sushi[i - 1]
    if current_sushi[left_sushi] == 1:
        current_count -= 1
    current_sushi[left_sushi] -= 1

    # 윈도우의 오른쪽 끝 초밥 추가
    right_sushi = sushi[(i + k - 1) % n]
    if current_sushi[right_sushi] == 0:
        current_count += 1
    current_sushi[right_sushi] += 1

    # 쿠폰 초밥을 포함한 최대 초밥 종류 계산
    if current_sushi[c] == 0:
        answer = max(answer, current_count + 1)
    else:
        answer = max(answer, current_count)

print(answer)