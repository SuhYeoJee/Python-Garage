# 25083
a = r'''         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |

'''
print(a)


# 3003
a = list(map(int,input().split()))
b = [1,1,2,2,2,8]

print(' '.join([str(b[i]-a[i])for i in range(len(b))]))

# 2444
N = int(input())
a = []
for i in range(N):
    k = (i+1)*2-1
    s = ' '*((N*2-1-k)//2) + '*'*k
    a.append(s)
[print(i) for i in a+a[:-1][::-1]]

# 10988
s = input()
n = len(s)//2
res = 1 if len(s)==1 else 1 if s[:n] == s[n*-1:][::-1] else 0
print(res)

# 1157
d = {}
for i in input().upper():
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

mval = max(d.values())
res = '?' if len([x for x in d.values() if x == mval])>1 else max(d,key=d.get)
print(res)

# 2941
print(len(input().replace('c=','_')\
.replace('c=','_').replace('c-','_')\
.replace('dz=','_').replace('d-','_')\
.replace('lj','_').replace('nj','_')\
.replace('s=','_').replace('z=','_')))

# 1316
N = int(input())
res = 0
for i in range(N):
    s = input()
    arr = [s[i] for i in range(len(s)) if i==0 or s[i] != s[i-1]]
    if len(arr) == len(set(arr)):
        res += 1
print(res)

# 25206
d = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0,
}

res = 0
a_sum = 0
for i in range(20):
    _,a,b = input().split()
    if b =='P':
        continue
    res += float(a)*d[b]
    a_sum += float(a)
print(res/a_sum)
