'''
1. 일단 50명의 손님 만들기
2. 손님 번호 n과 소요시간 t 정하기 (소요시간은 5-50분 사이의 난수)
3. 조건문을 사용하여 5-15분 사이의 승객은 O 표시하기
4. 반복
5. 총 탑승 승객 표시


for ()
i = 0
t = randint(5, 51)

if 5 <= t <= 15:
    print("[O] {}번째 손님 (소요시간 : {}분).format(n, t))
    i += 1
else:
    print("[] {}번째 손님 (소요시간 : {}분).format(n, t))

print("총 탑승 승객 : {} 분".format(i))
'''




from random import *

i = 0

for n in range(1, 51):
    t = randint(5, 51)
    if 5 <= t <= 15:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(n, t))
        i += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(n, t))

print("총 탑승 승객 : {} 분".format(i))

