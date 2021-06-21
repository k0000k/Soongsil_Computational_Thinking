
height = float(input('"키를 입력하세요(cm 단위)"'))
weight = float(input("몸무게를 입력하세요(kg 단위)"))

standard = (height - 100) * 0.9
ratio = weight / standard * 100

if ratio < 85:
    print("저체중입니다. 제 때에 많이먹고 운동하세요.")
    print("표준 몸무게는 %d kg입니다."%standard)
elif 85<=ratio<115 :
    print("정상 몸무게입니다. 지금 체중을 잘 유지하세요.")
    print("표준 몸무게는 %d kg입니다."%standard)
elif 115<=ratio<130:
    print("과체중 입니다. 약간 살이 쪘네요. 주 2일은 운동하세요.")
    print("표준 몸무게는 %d kg입니다."%standard)
elif ratio >= 130:
    print("비만입니다. 식사량을 줄이고 주 3일 이상 운동하세요.")
    print("표준 몸무게는 %d kg입니다."%standard)
