import random
a = []
for i in range(0,10):
    a.append(random.randint(0,49))
    i += 1
print(a)

def sort(array=a):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)    
        return sort(less)+equal+sort(greater)  
    else:
        return array

print(sort())
