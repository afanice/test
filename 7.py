import random
a, b = int(input()), int(input())
arr = [0]*10
i = 0
while(i < len(arr)):
    arr[i] = random.randint(0,100) 
    i += 1
print(arr)
print(arr[a] + arr[b])