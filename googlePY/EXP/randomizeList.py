import random

def randomize(arr):
     random.shuffle(arr)
     return arr

def randomize2(arr):
    for i in range(len(arr)):
        rand = random.randint(0,i+1)
        arr[i],arr[rand] = arr[rand],arr[i]
    return arr

print(randomize([1,2,2,3,4,5]))
print(randomize2([1,2,2,3,4,5]))
