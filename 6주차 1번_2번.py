#1번

def 이차함수(x):
    y=3*(x**2)+5*x+7
    return y

print(이차함수(15))

print(이차함수(20))

print(이차함수(25))


#2번

def 넓이(x,h):
    s=(1/2)*x*h
    return s

x=float(input('삼각형의 밑변의 길이를 입력하세요.'))
h=float(input('삼각형의 높이의 길이를 입력하세요.'))

print('삼각형의 넓이는 %.2f입니다.'%넓이(x,h))
