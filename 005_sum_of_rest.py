import sys
input = sys.stdin.readline


# 숫자 불러오기 ( 1 <= N <= 106, 2 <= M <= 103)

N, M = map(int, input().split())
number_series = list(map(int, input().split()))

S = [0] * N
C = [0] * M

S[0] = number_series[0]

answer = 0

for i in range(1,N):
    S[i] = S[i-1] + number_series[i]

for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(M):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)
