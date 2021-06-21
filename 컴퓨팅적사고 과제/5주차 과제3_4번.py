#3번

sum=0

for n in range(50,101):
    if (n%3==0) or (n%5==0):
        sum=sum+n
print(sum)


#4번

fruits=[]

while True:
    fruit=input('좋아하는 과일을 입력하세요. 0을 입력시, 과일입력이 종료되고 리스트가 출력됩니다.')
    if fruit=='0':
        print('과일 입력을 종료합니다.')
        break
    fruits.append(fruit)
print(fruits)
