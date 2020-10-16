# !/usr/bin/env python3

a = 72
b = 85

r = (b - a) / a * 100

print('小明的成绩提高了%.2f%s' % (r, '%'))

classmates = ['Michael', 'Jam', 'Lee']
print(classmates)
print(len(classmates))

classmates.append('Jack')
print(classmates[3])

classmates.insert(1, 'Andy')
print(classmates)

classmates[2] = 'King'
print(classmates)

print(classmates.pop(0))
print(classmates)

# list可变，duple不可变
duple = ('a', 'b')
print(duple)

# a = input('please enter you age: ')
# age = int(a)
# if age > 18:
#     print("成年人")
# else:
#     print("未成年人")

# 计算BMI，体重(kg) 除以 身高(m)的平方
weight = 79
height = 1.8
bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
    print('过轻')
elif 18.5 < bmi < 25:
    print('正常')
elif 25 < bmi < 28:
    print('过重')
elif 28 < bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello %s' % name)

# set可变，不可重复
s = {1, 1, 2, 3, 4, 4, 4}
print(s)
s.add(6)
print(s)
s.add(6)
print(s)

# dict 相当于map
d = {'a': 1, 'b': 2}
print(d.get('a'))
print(d.pop('a'))
print(d)
