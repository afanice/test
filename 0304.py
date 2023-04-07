'''
x = 2
y = 3
z = 5
def funcName(arg):
    arg = arg * 2
    return arg
print(funcName(x))
print(funcName(y))
print(funcName(z))
'''
'''
def f():
    return 1 + 1 
result = f()
print(result)
'''

'''
def f (x, y, z):
    return x + y + z
result = f(2, 4, 6)
print(result)
'''
'''
def compute_surface2(radius = 1, pi = 3.14159):
    return pi * radius * radius
print(compute_surface2(radius = 1, pi = 3.14))
print(compute_surface2(pi = 3.14, radius = 10))
print(compute_surface2(radius = 10))
'''
'''
def change_list(seq):
    seq[0] = 100
original = [0, 1, 2]
change_list(original)
print(original)
'''
'''
def find_square(integer1 = 2):
    result = integer1 * integer1
    return result
print(find_square())
'''

'''
def add_ints(integer1 = 2, integer2 = 4):
    result = integer1 + integer2
    return result
print(add_ints())
'''

'''
def take_power(integer1, integer2 = 2):
    result = 1
    for i in range(integer2):
        result = result * integer1
    return result
print(take_power(5))
'''

'''
a = 10
b = 3
def sum():
    c = a + b
    print('Сумма:', c)
def sub():
    d = a - b
    print('Разница:', d)
sub()
sum()
'''

'''
c = 10
def mul():
    global c
    c = c * 10
    print("Значение в функции:", c)
mul()
print('Значение вне функции:', c)
'''
'''
class StaticVar:
    @staticmethod
    def random(text):
        print(text)
        print('This class will print random text.')
StaticVar.random('This is a random class.')
'''
'''
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact)'''

'''X = 99
def f1():
    X = 88
    def f2():
        print(X)
    f2()
f1()
f2()'''

'''X = 99
def f1():
    X = 88
    def f2():
        X = 77
        print(X)
    f2()
    print(X)
f1()'''

X = 99
def f1():
    X = 88
    def f2():
        nonlocal X
        X = 77
        print(X)
    f2()
    print(X)
f1()
