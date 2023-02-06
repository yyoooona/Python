
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

# ******************************************************************************************
# 거듭제곱은 **
# ******************************************************************************************

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

# ******************************************************************************************
# format(f, ".2f") -> 소숫점 이하 2번째 자리까지 반올림한 값을 출력(즉, 3번째 자리에서 반올림한 값)
# ******************************************************************************************

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

# ******************************************************************************************
# 비트단위시프트연산자 이용 >>, <<
# ******************************************************************************************

# 6047
# a, b = map(int, input().split())
# print(a<<b)

# ******************************************************************************************
# a에 2의 b승 만큼 곱하는 것은 b만큼 좌측 시프트 연산 수행
# a를 b만큼 좌측으로 이동한 것은 (<<) a에 2의 b승만큼 곱해준 값과 같다
# ******************************************************************************************

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
# a, b = map(int, input().split())
# print(a!=b)

# 6052
# n = int(input())
# if n==0 : print("False")
# else : print("True")

# n = int(input())
# print(bool(n))

# ******************************************************************************************
# 정수값 0은 False(거짓)으로 판별되고 그 외의 값들은 True(참)으로 판별된다
# ******************************************************************************************

# 6053
# n = int(input())
# print(not bool(n))

# 6054
# a, b = map(int, input().split())
# print(bool(a) and bool(b))

# 6055
# a, b = map(int, input().split())
# print(bool(a) or bool(b))

# 6056
# a, b = map(int, input().split())
# if bool(a) == bool(b) : print("False")
# else : print("True")


# ******************************************************************************************
# 서로 같으면 False 다를 때만 True 출력 (XOR)
# print( (bool(a) and not bool(b)) or (not bool(a) and bool(b)) )
# ******************************************************************************************

# 6057
# a, b = map(int, input().split())
# print( (not bool(a) or bool(b)) and (bool(a) or not bool(b)) )

# ******************************************************************************************
# 서로 같을 때에만 True 하는 또 다른 방법
# print( (not bool(a) and not bool(b)) or (bool(a) and bool(b)) )
# ******************************************************************************************

# 6058
# a, b = map(int, input().split())
# print( not bool(a) and not bool(b) )

# 6059
# 비트 단위로 not 하여 출력하기
# a = int(input())
# print(~a)

# 6060
# 비트 단위로 and 하여 출력하기
# a, b = map(int, input().split())
# print(a & b)

# 6061
# a, b = map(int, input().split())
# print(a | b)

# 6062
# a, b = map(int, input().split())
# print(a^b)

# 6063
# a, b = map(int, input().split())
# print(a if a>b else b)

# ******************************************************************************************
# 3항 연산자
# x if C else y
# ******************************************************************************************

# 6064
# a, b, c = map(int, input().split())
# print(min(a, b, c))

# 6065
# a, b, c = map(int, input().split())
# if a%2 == 0 : print(a)
# if b%2 == 0 : print(b)
# if c%2 == 0 : print(c)

# 6066
# a = list(map(int, input().split()))
# for i in a :
#     if(i%2 == 0): print("even")
#     else : print("odd")

# 6067
# a = int(input())
# if a<0 and a%2 == 0: print("A")
# if a<0 and a%2 == 1: print("B")
# if a>0 and a%2 == 0: print("C")
# if a>0 and a%2 == 1: print("D")

# 6068
# a = int(input())
# if 90<=a<=100 : print('A')
# elif 70<=a<90 : print('B')
# elif 40<=a<70 : print('C')
# else : print('D')

# 6069
# c = input()
# if c is 'A' : print("best!!!")
# elif c == "B" : print("good!!")
# elif c is 'C' : print('run!')
# elif c is 'D' : print("slowly~")
# else : print("what?")

# ******************************************************************************************
# ' ' 나 " " 는 같이 쓰인다
# is 나 == 또한 같은 의미
# ******************************************************************************************

# 6070
# m = int(input())
# if m in (12, 1, 2) : print("winter")
# elif m in (3, 4, 5) : print("spring")
# elif m in (6, 7, 8) : print("summer")
# else : print("fall")

# 6071
# while 1 :
#     num = int(input())
#     if(num is not 0):
#         print(num)
#     elif(num is 0):
#         break

# 코드를 간결하게 하기 위해서 while문을 깨는 조건 (입력값이 0일때) 하나만 넣어줘도 됨!
# if num == 0 :
#    break
# else print(num)

# 6072
# num = int(input())
# while num is not 0 :
#     print(num)
#     num-=1

# 6073
# n = int(input())
# while n > 0 :
#     n-=1
#     print(n)

# 6074
# c = input()
# num = ord(c)
# st = ord('a')
#
# while st <= num :
#     print(chr(st), end = ' ')
#     st+=1

# ******************************************************************************************
# print( 출력할 내용, end = ' ' )
# print는 한줄 씩 여러 줄 출력, print(~~ , end = ' ') 한 칸씩 띄워서 한 줄에 모두 출력

# 아스키코드 문자 변환 : ord(문자), chr(숫자)
# ******************************************************************************************

