# # 2557
# print("Hello World")

# # 1000
# a,b = input().split(' ')
# print(int(a)+int(b))

# # 1001
# a,b = input().split(' ')
# print(int(a)-int(b))

# # 10998
# a,b = input().split(' ')
# print(int(a)*int(b))

# # 1008
# a,b = input().split(' ')
# print(int(a)/int(b))

# # 10869
# a,b = map(int,input().split())
# print(a+b,a-b,a*b,a//b,a%b,sep='\n')

# # 10926
# print(input()+'??!')

# # 18108
# # 불기 -> 서기 변환
# # 서기 = 불기 - 543
# print(int(input())-543)

# # 10430
# A,B,C = map(int,input().split())
# print((A+B)%C,((A%C) + (B%C))%C,(A*B)%C,((A%C)*(B%C))%C,sep='\n')

# # 2588
# a = int(input())
# b = input()
# print(a*int(b[2]),a*int(b[1]),a*int(b[0]),a*int(b),sep='\n')

# # 11382
# print(sum(map(int,input().split())))

# # 10171
# a = r'''\    /\
#  )  ( ')
# (  /  )
#  \(__)|
# '''
# print(a)

# # 10172
# a = r'''|\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|
# '''
# print(a)

# [문자열] -------------------------------------------------------------------------------------------
# #27866
# print(input()[int(input())-1])

# #2743
# print(len(input()))

# # 9086
# [print(f'{s[0]}{s[-1]}') for s in [input() for i in range(int(input()))]]

# # 11654
# print(ord(input()))

# # 11720
# count = int(input())
# num_str = input()
# print(sum([int(num_str[i]) for i in range(count)]))

# # 10809
# s = input()
# print(' '.join([str(s.find(chr(i))) for i in range(ord('a'),ord('z')+1)]))

# # 2675
# cnt = int(input())
# for i in range(cnt):
#     c,s = input().split()
#     result = ''
#     for j in range(len(s)):
#         result += s[j]*int(c)
#     print(result)
# # for문 써도 된다는걸 깨닫다..

# # 1152
# print(len(input().strip().split()))

# #2908
# a,b = map(lambda a: int(a[::-1]),input().split())
# res = a if a > b else b
# print(res)

# # 5622
# d = {
#     'ABC':3,
#     'DEF':4,
#     'GHI':5,
#     'JKL':6,
#     'MNO':7,
#     'PQRS':8,
#     'TUV':9,
#     'WXYZ':10
# }
# t = 0
# for i in input():
#     for k,v in d.items():
#         if i in k:
#             t+=v
# print(t)

# # 11718
# # sys.stdin.read() 를 처음써봐서 헤맴
# import sys
# print(sys.stdin.read())

# [배열] -------------------------------------------------------------------------------------------

# # 10807
# input()
# print(list(map(int,input().split())).count(int(input())))

# # 10871
# n,x = map(int,input().split())
# a = list(map(int,input().split()))
# print(' '.join([str(z) for z in a if z < x]))

# # 10818
# input()
# a = list(map(int,input().split()))
# print(min(a),max(a))

# # 2562
# a = [int(input()) for x in range(9)]
# print(max(a),a.index(max(a))+1,sep='\n')

# # 10810
# n,m = map(int,input().split())
# arr = ['0']*n

# for _ in range(m):
#     i,j,k = map(int,input().split())
#     for idx in range(i-1,j):
#         arr[idx] = str(k)
# print(' '.join(arr))

# # 10813
# n,m = map(int,input().split())
# arr = [str(x+1) for x in range(n)]

# for _ in range(m):
#     i,j = map(lambda a:int(a)-1,input().split())
#     t = arr[i]
#     arr[i] = arr[j]
#     arr[j] = t
# print(' '.join(arr))

# # 5597
# arr = [int(input()) for _ in range(28)]
# [print(x) for x in list(map(lambda a:int(a)+1,range(30))) if x not in arr]

# # 3052
# arr = [int(input())%42 for _ in range(10)]
# print(len(list(set(arr))))

# # 10811
# n,m = map(int,input().split())
# arr = [str(x+1) for x in range(n)]

# for _ in range(m):
#     i,j = map(lambda a:int(a)-1,input().split())
#     t = arr[i:j+1][::-1]
#     for idx in range(len(t)):
#         arr[i+idx] = t[idx]
# print(' '.join(arr))


# # 1546
# input()
# arr = list(map(int,input().split()))
# M = max(arr)
# new_arr = [a/M*100 for a in arr]
# print(sum(new_arr)/len(new_arr))

# [반복문] -------------------------------------------------------------------------------------------

# # 2739
# N = int(input())
# for i in range(9):
#     print(f'{N} * {i+1} = {N*(i+1)}')

# # 10950
# for i in range(int(input())):
#     print(sum(map(int,input().split())))

# # 8393
# print(sum([x+1 for x in range(int(input()))]))

# # 25304
# X = int(input())
# N = int(input())

# print('Yes') if X == sum([a*b for a,b in [map(int,input().split()) for _ in range(N)]]) else print('No')

# # 25314
# print('long ' * int(int(input())/4) + 'int')

# # 15552
# # 빠른입출력 
# import sys
# for _ in range(int(sys.stdin.readline().strip())):
#     sys.stdout.write(str(sum(map(int,sys.stdin.readline().strip().split())))+'\n')

# # 11021
# for i in range(int(input())):
#     print(f'Case #{i+1}: {sum(map(int,input().split()))}')

# # 11022
# for i in range(int(input())):
#     A,B = map(int,input().split())
#     print(f'Case #{i+1}: {A} + {B} = {A+B}')

# # 2438
# [print('*'*(i+1)) for i in range(int(input()))]

# # 2439
# N = int(input())
# [print(' '*(N-(i+1)) + '*'*(i+1)) for i in range(N)]

# # 10950
# while(1):
#     res = sum(map(int,input().split()))
#     if res:
#         print(res)
#     else:
#         break

# # 10951
# vs콘솔에서 eof 주기: ^z
# import sys
# print('\n'.join([str(sum(map(int,x.strip().split())))for x in sys.stdin.read().splitlines()]))


# [조건문] -------------------------------------------------------------------------------------------

# # 1330
# A,B = map(int,input().split())
# print('>') if A > B else print('==') if A == B else print('<')

# # 9498
# s = int(input())
# res = 'A' if s > 89 else 'B' if s > 79 else 'C' if s > 69 else 'D' if s > 59 else 'F'
# print(res)

# # 2753
# y = int(input())
# res = 1 if y%4==0 and y%100 else 1 if y%400==0 else 0
# print(res)

# # 14681
# x = int(input())
# y = int(input())

# res = [1,3] if x*y > 0 else [4,2]
# print(res[0]) if x > 0 else print(res[1])

# # 2884
# H,M = map(int,input().split())
# M -= 45
# if M < 0:
#     M+=60
#     H-=1
# if H < 0:
#     H+=24
# print(H,M)

# # 2525
# H,M = map(int,input().split())
# T = int(input())
# H += T//60
# M += T%60

# if M > 59:
#     M-=60
#     H+=1
# if H > 23:
#     H-=24
# print(H,M)

# # 2480
# a = list(map(int,input().split()))
# s = set(a)
# res = 10000 + a[0]*1000 if len(s)==1 \
#     else 1000 + (a[0] if a[1] != a[2] else a[1])*100 if len(s)==2 \
#     else max(s)*100
# print(res)

# [심화 1] -------------------------------------------------------------------------------------------

# # 25083
# a = r'''         ,r'"7
# r`-_   ,'  ,/
#  \. ". L_r'
#    `~\/
#       |
#       |

# '''
# print(a)


# # 3003
# a = list(map(int,input().split()))
# b = [1,1,2,2,2,8]

# print(' '.join([str(b[i]-a[i])for i in range(len(b))]))

# # 2444
# N = int(input())
# a = []
# for i in range(N):
#     k = (i+1)*2-1
#     s = ' '*((N*2-1-k)//2) + '*'*k
#     a.append(s)
# [print(i) for i in a+a[:-1][::-1]]

# # 10988
# s = input()
# n = len(s)//2
# res = 1 if len(s)==1 else 1 if s[:n] == s[n*-1:][::-1] else 0
# print(res)

# # 1157
# d = {}
# for i in input().upper():
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# mval = max(d.values())
# res = '?' if len([x for x in d.values() if x == mval])>1 else max(d,key=d.get)
# print(res)

# # 2941
# print(len(input().replace('c=','_')\
# .replace('c=','_').replace('c-','_')\
# .replace('dz=','_').replace('d-','_')\
# .replace('lj','_').replace('nj','_')\
# .replace('s=','_').replace('z=','_')))

# # 1316
# N = int(input())
# res = 0
# for i in range(N):
#     s = input()
#     arr = [s[i] for i in range(len(s)) if i==0 or s[i] != s[i-1]]
#     if len(arr) == len(set(arr)):
#         res += 1
# print(res)

# # 25206
# d = {
#     'A+':4.5,
#     'A0':4.0,
#     'B+':3.5,
#     'B0':3.0,
#     'C+':2.5,
#     'C0':2.0,
#     'D+':1.5,
#     'D0':1.0,
#     'F':0.0,
# }

# res = 0
# a_sum = 0
# for i in range(20):
#     _,a,b = input().split()
#     if b =='P':
#         continue
#     res += float(a)*d[b]
#     a_sum += float(a)
# print(res/a_sum)
