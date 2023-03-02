print ("시험 과목수를 입력하세요")
n = int(input())
print ("과목 수 만큼 시험 점수를 입력하시오(띄어쓰기로 구분하시오)")
mylist = list(map(int,input().split()))

if n == len(mylist):
    mymax = max(mylist)
    sum = sum(mylist)
    print(sum*100 / mymax / int(n))
else:
    print ('시험 과목 수와 시험 점수 숫자가 일치하지 않습니다.')