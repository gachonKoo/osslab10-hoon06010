import sys

number = int(sys.argv[1])
divisors = []

# 먼저 모든 약수를 리스트에 저장
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(str(i)) # 문자열로 저장

# 리스트의 모든 요소를 ' ' 공백으로 연결하여 한 번에 출력
print(" ".join(divisors))

# 원본 코드의 마지막 print() 문은 불필요해지므로 삭제
