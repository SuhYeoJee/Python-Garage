# 10807
input()
print(list(map(int,input().split())).count(int(input())))

# 10871
n,x = map(int,input().split())
a = list(map(int,input().split()))
print(' '.join([str(z) for z in a if z < x]))

# 10818
input()
a = list(map(int,input().split()))
print(min(a),max(a))

# 2562
a = [int(input()) for x in range(9)]
print(max(a),a.index(max(a))+1,sep='\n')

# 10810
n,m = map(int,input().split())
arr = ['0']*n

for _ in range(m):
    i,j,k = map(int,input().split())
    for idx in range(i-1,j):
        arr[idx] = str(k)
print(' '.join(arr))

# 10813
n,m = map(int,input().split())
arr = [str(x+1) for x in range(n)]

for _ in range(m):
    i,j = map(lambda a:int(a)-1,input().split())
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
print(' '.join(arr))

# 5597
arr = [int(input()) for _ in range(28)]
[print(x) for x in list(map(lambda a:int(a)+1,range(30))) if x not in arr]

# 3052
arr = [int(input())%42 for _ in range(10)]
print(len(list(set(arr))))

# 10811
n,m = map(int,input().split())
arr = [str(x+1) for x in range(n)]

for _ in range(m):
    i,j = map(lambda a:int(a)-1,input().split())
    t = arr[i:j+1][::-1]
    for idx in range(len(t)):
        arr[i+idx] = t[idx]
print(' '.join(arr))


# 1546
input()
arr = list(map(int,input().split()))
M = max(arr)
new_arr = [a/M*100 for a in arr]
print(sum(new_arr)/len(new_arr))
