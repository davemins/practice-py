#방법1
print("a" + "b")

print("나는 %d살입니다." % 20)

print("나는 %s을 좋아해요." % '파이썬')
print("Apple 은 %c로 시작해요." % "A")

# %s 를 놓으면 모두 사용이 가능하다

print("I like %s and %s." %("red", "green"))

#방법2
print("I am {} years old. " .format(20))

#방법3
print("I am {age} yeras old, and I like {color} color." .format(age = 20, color ="red"))

#방법4
age = 20
color = "red"
print(f"I am {age} years old. And I like {color} color.")