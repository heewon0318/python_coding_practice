import sys
input = sys.stdin.readline



print ('데이터 개수, 질문의 개수')
n, m =map(int,input().split())

print ('숫자 배열을 입력하세요 (첫번째 데이터 개수 만큼)')
numbers = list(map(int,input().split()))


prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

print('구간의 시작과 끝을 입력하세요')
for j in range(m):
    start, end = map(int, input().split())
    print (prefix_sum[end] - prefix_sum[start-1])
