# 2557
print("Hello World")

# 1000
a,b = input().split(' ')
print(int(a)+int(b))

# 1001
a,b = input().split(' ')
print(int(a)-int(b))

# 10998
a,b = input().split(' ')
print(int(a)*int(b))

# 1008
a,b = input().split(' ')
print(int(a)/int(b))

# 10869
a,b = map(int,input().split())
print(a+b,a-b,a*b,a//b,a%b,sep='\n')

# 10926
print(input()+'??!')

# 18108
# 불기 -> 서기 변환
# 서기 = 불기 - 543
print(int(input())-543)

# 10430
A,B,C = map(int,input().split())
print((A+B)%C,((A%C) + (B%C))%C,(A*B)%C,((A%C)*(B%C))%C,sep='\n')

# 2588
a = int(input())
b = input()
print(a*int(b[2]),a*int(b[1]),a*int(b[0]),a*int(b),sep='\n')

# 11382
print(sum(map(int,input().split())))

# 10171
a = r'''\    /\
 )  ( ')
(  /  )
 \(__)|
'''
print(a)

# 10172
a = r'''|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''
print(a)
