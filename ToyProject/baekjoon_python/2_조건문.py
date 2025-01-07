# 1330
A,B = map(int,input().split())
print('>') if A > B else print('==') if A == B else print('<')

# 9498
s = int(input())
res = 'A' if s > 89 else 'B' if s > 79 else 'C' if s > 69 else 'D' if s > 59 else 'F'
print(res)

# 2753
y = int(input())
res = 1 if y%4==0 and y%100 else 1 if y%400==0 else 0
print(res)

# 14681
x = int(input())
y = int(input())

res = [1,3] if x*y > 0 else [4,2]
print(res[0]) if x > 0 else print(res[1])

# 2884
H,M = map(int,input().split())
M -= 45
if M < 0:
    M+=60
    H-=1
if H < 0:
    H+=24
print(H,M)

# 2525
H,M = map(int,input().split())
T = int(input())
H += T//60
M += T%60

if M > 59:
    M-=60
    H+=1
if H > 23:
    H-=24
print(H,M)

# 2480
a = list(map(int,input().split()))
s = set(a)
res = 10000 + a[0]*1000 if len(s)==1 \
    else 1000 + (a[0] if a[1] != a[2] else a[1])*100 if len(s)==2 \
    else max(s)*100
print(res)