'''
ref : https://leetcode.com/discuss/interview-question/399386/
input :
3


3
banana 90
apple 100
apple 260

5
grapefruit 120
grape 200
grapefruit 150
grapefruit 150
grape 180

2
apple 100
apple 101

'''

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

lines = [el for el in lines if el != '']
currLine = 0
n = int(lines[currLine])
finalOutPut = ''
for i in range(n):
    currLine += 1
    nFruits = int(lines[currLine])
    fruits = {}
    for j in range(nFruits):
        currLine += 1
        fruitName, fruitPrice = lines[currLine].split()
        fruitPrice = int(fruitPrice)
        if not fruits.get(fruitName):
            fruits[fruitName] = {'name':fruitName,'count':1,'min':fruitPrice,'max':fruitPrice,'total':fruitPrice,'avg':fruitPrice}

        else:
            fruits[fruitName]['count'] += 1
            fruits[fruitName]['min'] = min(fruits[fruitName]['min'],fruitPrice)
            fruits[fruitName]['max'] = max(fruits[fruitName]['max'],fruitPrice)
            fruits[fruitName]['total'] += fruitPrice
            fruits[fruitName]['avg'] = fruits[fruitName]['total'] // fruits[fruitName]['count']

    sortedNames = sorted(fruits.keys())
    finalOutPut += 'Case #'+str(i+1)+":\n"
    for name in sortedNames:
        finalOutPut += name+" "+str(fruits[name]['min'])+" "+str(fruits[name]['max'])+" "+str(fruits[name]['avg'])+'\n'
    finalOutPut += '\n'

print(finalOutPut)
