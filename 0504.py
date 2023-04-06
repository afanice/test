'''
list = [['a',1],['b',2]]
dict(list)
'''
'''
x = 'Строка'
print(list(x))
'''
'''
print(eval('2+2'))
'''
'''
list1 = [3, 5, 4, 8, 6, 33, 22, 18, 76, 1]
result = list(filter(lambda x: (x%2 != 0), list1))
print(result)
'''

#  28n+30k+31m=365

total = 0
for n in range(1, 7):
    for k in range(1, 7):
        if 28 * n + 30 * k + 31 == 365:
            total += 1
            print('n=', n, 'k=', k)