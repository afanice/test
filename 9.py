


a = ['']*1
n = int(input())
while(n>0):
    if n % 2 == 0:
        a.append('0')
    else:
        a.append('1')
    n = n//2
i = 1
while(i<=len(a)):
    print(a[-i], end = '')
    i += 1


'''
a = input()
if len(a) % 2 == 0:
    for c in a:
        print(c, end = ' ')
elif len(a) %2 != 0:
    for c in a:
        print(c)
'''

'''
n = int(input())
i = 0
m = [0]*n
while i < n:
    m[i] = int(input())
    i += 1
print(min(m))
'''

'''
n = int(input('число '))
i = 1
m = 1
while i <= n:
    if i%2 == 0:
        m = m*i
    i +=1
if m>1:
    print(m)
else:
    print('0')
'''

'''
n, x = int(input()), int(input())
a = n - x % n
print(a)
'''

'''
a = (input())
if a != ' ':
    if (int(a) % 3 == 0) or (len(a) % 3 == 0):
        print("Да")
    else:
        print('Нет')
else:
    print('Вы не ввели цифры')
'''

'''
a, b, c = int(input()), int(input()), int(input())
if a in b or a in c:
    print(a)
elif b in a or b in c:
    print(a)
else:
    print('все числа разные')
'''

'''
a, b, c = int(input()), int(input()), int(input())
if a==b==c:
    print(a)
elif a==b or b==c:
    print(b)
elif a==c or a==b:
    print(a)
elif a==c or b==c:
    print(c)
elif a!=b!=c:
    print("Все числа разные")
'''

'''
a = int(input())
if a == 1 or a == 21:
    print(a, 'стул')
elif 1 < a < 5:
    print(a, 'стула')
elif 5 <= a < 21 or a == 0:
    print(a, 'стульев')
'''