print ("숫자의 개수를 입력하시오")
n = int(input())
print ("0~9 숫자를 위에 입력한 수만큼 입력하시오")
numbers = list(input())
sum = 0

if n == len(numbers):
    for i in numbers:
        sum = sum + int(i)
    print(sum)
else:
    print("입력한 숫자의 개수가 설정값과 다릅니다.")

# a



