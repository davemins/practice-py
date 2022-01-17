# Quiz 4

# from random import *

# lst = [1,2,3,4,5]
# print(lst)

# shuffle(lst)
# print(lst)

# print(sample(lst, 1))

'''
Let's think about it.

comments = 20

chicken = 1
coffee = 3

1. 배열 선언 (1-20)
2. 무작위로 섞기
3. 값 출력

output
print("-- 당첨자 발표 --")
print("치킨 당첨자 : " + )
print("커피 당첨자 : " + )
print("-- 축하합니다 --")
'''
from random import *

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# lst = range(1,21)
# lst = list(lst) 
shuffle(lst)
chicken = lst[0]

print("-- 당첨자 발표 --")
print("치킨 당첨자 : " + str(chicken))
print("커피 당첨자 : ", sample(lst, 3))
print("-- 축하합니다 --")