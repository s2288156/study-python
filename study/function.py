for i in range(3):
    print(i)

a = ['Marry', 'Tom', 'Jone', 'Kobe']
for i in range(len(a)):
    print(i, a[i])


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('>>>>>>> bad operand type')
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-3))


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes',):
            return True
        if ok in ('n', 'no', 'nop', 'nope',):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder, ', times has ', retries)


# ask_ok('Do you Really want to quit?')


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def calc(*number):
    result = 0
    for n in number:
        result = result + n
    return result


l = [1, 4, 6]
# print(calc((1, 3, 4)))
print(calc(*l))
