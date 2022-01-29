'''
1. Start time, End time 입력
2. Current time 자동으로 반환
3. Elapsed time, Remaining time 계산
4. Press 누르면 출력
3. Elapsed time, Remaining time 출력
'''



'''
뺄셈을 어떻게 하지?
elapsed = current - 07:52 = current - ti(hours=7, minute=52)
remaining = 16:52-12:22 = timedelta(hours=16, minute=52)


import datetime

current = datetime.datetime.now()
print(current.strftime("%X"))

elapsed = datetime(2021, 12, 31, 13, 35, 42, 657813)

'''


'''
import datetime

current = datetime.datetime.now()

while choice != n:
    choice = input("Press : ")
        elapsed = current - datetime(2022, 01, 17, 07, 52, 42, 657813)
        remaining = datetime(2022, 01, 17, 16, 52, 42, 657813) - current
        print("Current - {} / {} Elapsed , {} Remaining".format(current, elapsed, remaining))

print("enough")
'''

import datetime

current = datetime.datetime.now()
elapsed = datetime(2022, 01, 17, 07, 52, 42, 657813)
print(ela)
remaining = datetime(2022, 01, 17, 16, 52, 42, 657813) - current

while choice != n:
    choice = input("Press : ")

        print("Current - {} / {} Elapsed , {} Remaining".format(current, elapsed, remaining))

print("enough")