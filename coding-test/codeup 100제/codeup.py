
# 6018
# a, b = input().split(':')
# print(f"{a}:{b}")

# 6019
# y, m, d = input().split('.')
# print(f"{d}-{m}-{y}")

# 6020
# a, b = input().split('-')
# print(f"{a}{b}")

# 6021
# s = input()
# for i in range(len(s)):
#     print(s[i])

# 6022
# s = input()
# y = s[0:2]
# m = s[2:4]
# d = s[4:6]
# print(y, m, d)

# 6023
# h, m, s = input().split(':')
# print(m)

# 6024
# a, b = input().split()
# print(a + b)

# 6025
# a, b = map(int, input().split())
# c = a + b
# print(f"{a+b}")
# print(a+b)
# print(c)

# 6026
# a = float(input())
# b = float(input())
# print(a + b)

# 6027
# num = int(input())
# print('%x'%num)

# 6028
# num = int(input())
# print('%X'%num)

# 6029
# num = int(input(), 16)
# print('%o'%num)

# 6030
# num = ord(input())
# print(num)

# 6031
# c = int(input())
# print(chr(c))

# 6032
# num = int(input())
# print(-num)

# 6033
# c = ord(input())
# print(chr(c+1))

# 6034
# a, b = map(int, input().split())
# print(a-b)

# 6035
# a, b = map(float, input().split())
# print(a*b)

# 6036
# c, num = input().split()
# num = int(num)
# print(c*num)
# 위의 두 줄을 한 줄로
# print(c*int(num))

# 6037
# num = int(input())
# s = input()
# print(s*num)

# 6038
# a, b = map(int, input().split())
# print(a**b)
# 거듭제곱은 **

# 6039
# f1, f2 = map(float, input().split())
# print(f1**f2)

# 6040
# a, b = map(int, input().split())
# print(a//b)

# 6041
# a, b = map(int, input().split())
# print(a%b)

# 6042
# f = float(input())
# print(format(f, ".2f"))
# format(f, ".2f") -> 소숫점 이하 2번째 자리까지 반올림한 값을 출력(즉, 3번째 자리에서 반올림한 값)

# 6043
# f1, f2 = map(float, input().split())
# print(format(f1/f2, ".3f"))

# 6044
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b, ".2f"))

# 6045
# a, b, c = map(int, input().split())
# sum = a+b+c
# print(sum, format(sum/3, ".2f"))

# 6046
# num = int(input())
# print(num<<1)
# 비트단위시프트연산자 이용 >>, <<

# 6047
# a, b = map(int, input().split())
# print(a<<b)
# a에 2의 b승 만큼 곱하는 것은 b만큼 좌측 시프트 연산 수행
# a를 b만큼 좌측으로 이동한 것은 (<<) a에 2의 b승만큼 곱해준 값과 같다

# 6048
# a, b = map(int, input().split())
# print(a<b)
# if a<b : print("True")
# else : print("False")

# 6049
# a, b = map(int, input().split())
# print(a==b)

# 6050
# a, b = map(int, input().split())
# if a <= b : print("True")
# else : print("False")

# 6051