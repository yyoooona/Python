
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

# 6075
# st = 0
# n = int(input())
# while st <= n :
#     print(st);
#     st += 1

# 6076
# n = int(input())
# for i in range(0, n + 1):
#     print(i)

# ******************************************************************************************
# for i in range(n+1) :
# range(n+1)은 0부터 n까지의 숫자 출력

# range(끝)
# range(시작, 끝)
# range(시작, 끝, 증감)
# ******************************************************************************************

# 6077
# n = int(input())
# sum = 0           # 합계
# for i in range(1, n+1):
#     if i%2 == 0 : # 짝수
#         sum += i
# print(sum)

# 6078
# 1)
# tgt_num = ord('q')
# while 1 :
#     m = ord(input())
#     if m != tgt_num :
#         print(chr(m))
#     else : # m == tgt_num 일 경우
#         print(chr(m))
#         break

# 2)
# while True :
#     c = input()
#     if c == 'q':
#         print(c)
#         break
#     else :
#         print(c)

# 3) 더 짧은 모범답안 -> 공통되는 코드는 앞이나 뒤로 빼기
# while True :
#     c = input()
#     print(c)
#     if c == 'q':
#         break

# ******************************************************************************************
# 아스키코드로 변환할 필요 없이 문자끼리 비교
# ******************************************************************************************

# 6079
# n = int(input())
# sum = 0
# for i in range(1, 1000):
#     if(sum + i < n):
#         sum += i
#     else :
#         print(i)
#         break

# 모범답안
# n = int(input())
# sum = 0
# tgt = 0
# while sum < n:
#     tgt += 1
#     sum += tgt
#
# print(tgt)

# 6080
# n, m = map(int, input().split())
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

# 6081
# n = int(input(), 16)
# for i in range(1, 16):
#     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# ******************************************************************************************
# 1. 16진수 int로 받기
#    n = int(input(), 16)

# 2. 16진수 곱 출력 (곱한 값도 16진수로)
#    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
#    sep 은 구분자
# ******************************************************************************************

# 6082
# n = int(input())
# for i in range(1, n+1):
#     if i%10 in (3, 6, 9):
#         print('X', end = ' ')
#     else :
#         print(i, end = ' ')

# 6083
# i, j, k = map(int, input().split())
# count = 0
# for a in range(i):
#     for b in range(j):
#         for c in range(k):
#             print(a, b, c)
#             count+=1
# print(count)

# 6084
# h, b, c, s = map(int, input().split())
# mb = ((h*b*c*s)/8)/(1024**2)

# print(format(mb, ".1f") + ' MB')
# print(f"{format(mb, '.1f')} MB")
# print(round(mb, 1), 'MB')

# ******************************************************************************************
# format(f, ".2f") -> 소숫점 이하 2번째 자리까지 반올림한 값을 출력(즉, 3번째 자리에서 반올림한 값)
# print(f"{a}:{b}")

# round 반올림 함수
# print(round(h*b*c*s/8/1024/1024, 1), "MB")
# ******************************************************************************************

# 6085
# w, h, b = map(int, input().split())
# print(format(round((((w*h*b)/8)/1024)/1024, 2), '.2f'), 'MB')

# 6086
# n = int(input())
# s = 0 # 합
# c = 1
# while True:
#     if s >= n :
#         print(s)
#         break
#     s += c
#     c +=1

# 6087
# n = int(input())
# for i in range(1, n+1):
#     if i%3 == 0:
#         continue
#     print(i, end= ' ')

# 6088
# st, ad, tgt = map(int, input().split())
# for _ in range(tgt-1):
#     st += ad
# print(st)

# 6089
# a, r, n = map(int, input().split())
# for _ in range(n-1):
#     a*=r
# print(a)

# 6090
# a, m, d, n = map(int, input().split())
# for _ in range(n-1):
#     a *= m
#     a += d
# print(a)

# 6091
# a, b, c = map(int, input().split())
# st = min(a, b, c)
# while True:
#     if st%a==0 and st%b==0 and st%c==0 :
#         print(st)
#         break
#     st+=1

# ******************************************************************************************
# min 함수
# min(숫자, list 등)
# ******************************************************************************************

# 6092
# n = int(input())
# a = list(map(int, input().split()))
# # a리스트 입력 test
# # for i in range(n):
# #     print(a[i], end=' ')
# b = [0 for i in range(23)]
# for j in a:
#     b[j-1]+=1
# for k in b:
#     print(k, end=' ')

# ******************************************************************************************
# 길이가 정해진 list 만들기
# list = [0 for i in range(n)]
# 리스트 길이를 지정하고 0으로 초기화

# 또 다른 방법
# d = []
# for i in range(24) :
#     d.append(0)
# ******************************************************************************************

# 6093
# n = int(input())
# a = list(map(int, input().split()))
#
# for i in range(len(a)):
#     print(a[len(a)-1-i], end=' ')
