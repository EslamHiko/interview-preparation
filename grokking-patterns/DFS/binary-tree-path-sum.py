'''
Problem Statement #
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

  1
  2
  3
  4
  5
  6
  7
 S: 10Output: trueExplaination: The path with sum '10' is highlighted
 Example 1:
 Example 2:
  12
  7
  1
  9
  10
  5
 S: 23Output: trueExplaination: The path with sum '23' is highlighted  S: 16Output: falseExplaination: There is no root-to-leaf path with sum '16'.
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None

head = Node(12)
head.left = Node(7)
head.right = Node(1)
head.left.left = Node(9)
head.right.left = Node(10)
head.right.right = Node(5)

def sol(head,sum):
    def dfs(n,currSum):
        if n is None:
            return False
        currSum += n.val
        # must be a leaf
        if currSum == sum and n.left is None and n.right is None:
            return True
        return dfs(n.right,currSum) or dfs(n.left,currSum)

    return dfs(head,0)

print(sol(head,23))
print(sol(head,16))
