import random

a = []
j = 0
s = 0

for i in range(0,10):
    a.append(random.randint(0,49))
    i += 1

print(a)
a.append(1)

while s <= 9 :
    s = 0
    for i in range(0,10):
        if a[i+1] < a[i] and i < 9:
            j = a[i]
            a[i] = a[i+1] 
            a[i+1] = j
        else: s += 1
    
    # s = 0
    # for i in range(0,10):
    #     if (a[i+1] > a[i] and i < 9) or a[i] == a[i+1]:
    #         s += 1

a.pop()
print(a)