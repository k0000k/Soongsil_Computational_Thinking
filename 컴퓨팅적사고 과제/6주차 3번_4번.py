#3번

def 학점(score):
    if 90<=score<=100:
        학점='A'
    elif 80<=score<=89:
        학점='B'
    elif 70<=score<=79:
        학점='C'
    elif 60<=score<=69:
        학점='D'
    else:
        학점='F'
    return 학점

score=int(input('0부터 100까지의 정수로 점수를 입력하세요'))

print('%s학점입니다.'%학점(score))
    


#4번

def 판별(x):
    y=x%2
    return y

x=int(input('정수를 입력하세요.'))

y=판별(x)

if y==0:
    print('짝수입니다.')
else:
    print('홀수입니다.')
