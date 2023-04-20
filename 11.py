'''
a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a > b:
        a = a % b
        print(a)
    else:
        b = b % a
        print(b) 
print(a + b)
'''
'''
a = input()
k = 0
for c in a:
    if c == '=':
    k += 1
print(k)
'''

'''
n = int(input())
k = int(input())
if n % k == 0:
    print('')
else:
    a = n%k
    b = '!'
    print(a*b)
'''


