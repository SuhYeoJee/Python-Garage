#27866
print(input()[int(input())-1])

#2743
print(len(input()))

# 9086
[print(f'{s[0]}{s[-1]}') for s in [input() for i in range(int(input()))]]

# 11654
print(ord(input()))

# 11720
count = int(input())
num_str = input()
print(sum([int(num_str[i]) for i in range(count)]))

# 10809
s = input()
print(' '.join([str(s.find(chr(i))) for i in range(ord('a'),ord('z')+1)]))

# 2675
cnt = int(input())
for i in range(cnt):
    c,s = input().split()
    result = ''
    for j in range(len(s)):
        result += s[j]*int(c)
    print(result)
# for문 써도 된다는걸 깨닫다..

# 1152
print(len(input().strip().split()))

#2908
a,b = map(lambda a: int(a[::-1]),input().split())
res = a if a > b else b
print(res)

# 5622
d = {
    'ABC':3,
    'DEF':4,
    'GHI':5,
    'JKL':6,
    'MNO':7,
    'PQRS':8,
    'TUV':9,
    'WXYZ':10
}
t = 0
for i in input():
    for k,v in d.items():
        if i in k:
            t+=v
print(t)

# 11718
# sys.stdin.read() 를 처음써봐서 헤맴
import sys
print(sys.stdin.read())
