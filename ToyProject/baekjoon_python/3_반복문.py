# 2739
N = int(input())
for i in range(9):
    print(f'{N} * {i+1} = {N*(i+1)}')

# 10950
for i in range(int(input())):
    print(sum(map(int,input().split())))

# 8393
print(sum([x+1 for x in range(int(input()))]))

# 25304
X = int(input())
N = int(input())
print('Yes') if X == sum([a*b for a,b in [map(int,input().split()) for _ in range(N)]]) else print('No')

# 25314
print('long ' * int(int(input())/4) + 'int')

# 15552
# 빠른입출력 
import sys
for _ in range(int(sys.stdin.readline().strip())):
    sys.stdout.write(str(sum(map(int,sys.stdin.readline().strip().split())))+'\n')

# 11021
for i in range(int(input())):
    print(f'Case #{i+1}: {sum(map(int,input().split()))}')

# 11022
for i in range(int(input())):
    A,B = map(int,input().split())
    print(f'Case #{i+1}: {A} + {B} = {A+B}')

# 2438
[print('*'*(i+1)) for i in range(int(input()))]

# 2439
N = int(input())
[print(' '*(N-(i+1)) + '*'*(i+1)) for i in range(N)]

# 10950
while(1):
    res = sum(map(int,input().split()))
    if res:
        print(res)
    else:
        break

# 10951
# vs콘솔에서 eof 주기: ^z
import sys
print('\n'.join([str(sum(map(int,x.strip().split())))for x in sys.stdin.read().splitlines()]))