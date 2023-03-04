# 내가 만든 코딩
# 2차원 배열의 크기, 구간 합 질의의 개수 입력 받기
array_n, ask_n = map(int,input().split())

matrix_a = []

배열 입력 받기
for i in range(array_n):
    matrix_row = list(map(int, input().split()))
    matrix_a.append(matrix_row)

answer_a = []


질의 범위 입력 받고 계산 하기
for i in range(ask_n):
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0
    for j in range(x1-1, x2):
        for k in range(y1-1, y2):
            sum = sum + matrix_a[j][k]

    answer_a.append(sum)

# 답 출력하기
for i in answer_a:
    print(i)

# 정답
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = [[0]*(n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        #합 배열 구하기
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    #구간 합 배열로 질의에 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)