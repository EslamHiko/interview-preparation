'''
input:
3
1
2 2
1 2 2 2
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

# constructing the BST
currLine = 0
levels = int(lines[currLine])
root = None
nodes = []
for i in range(levels):
    currLine += 1
    nodes += [int(el) for el in lines[currLine].split()]

def constructBSTfromArr(nodes,root,currIndex):
    if currIndex < len(nodes):
        currNode = Node(nodes[currIndex])
        root = currNode
        root.left = constructBSTfromArr(nodes,root.left,2*currIndex+1)
        root.right = constructBSTfromArr(nodes,root.right,2*currIndex+2)
    return root

count = 0
def countUniValNodes(root):
    global count

    if root.left is None and root.right is None:
        count += 1
        return True

    # flag to determine is it valid uni or not
    flag = True

    if root.left is not None:
        flag = countUniValNodes(root.left) and flag and root.left.val == root.val

    if root.right is not None:
        # checking flag here again because both root.left & root.right must be equal to root.val
        flag = countUniValNodes(root.right) and flag and root.right.val == root.val

    if flag:
        count += 1

    return flag

root = constructBSTfromArr(nodes,root,0)
countUniValNodes(root)


print(count)
