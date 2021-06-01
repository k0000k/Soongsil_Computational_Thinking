#1번 while 사용

import sys

n=int(input('2부터 9까지 중에서 정수 하나를 입력하세요.'))
if not(2<=n<=9):
    print('잘못된 값이 입력 되었습니다. 프로그램을 종료합니다.')
    sys.exit()

m=1
while m<=9:
    print('%d x %d = %d' %(n,m,n*m))
    m=m+1


#1번 for 사용

import sys

n=int(input('2부터 9까지 중에서 정수 하나를 입력하세요.'))
if not(2<=n<=9):
    print('잘못된 값이 입력 되었습니다. 프로그램을 종료합니다.')
    sys.exit()

for m in range(1,10):
    print('%d x %d = %d' %(n,m,n*m))


#2번

n=30
sum=0

while n<=70:
    if n%3==0:
        sum=sum+n
    n=n+1
print(sum)
