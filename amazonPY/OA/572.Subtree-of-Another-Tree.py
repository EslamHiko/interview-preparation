'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
class TreeNode:
    def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

def sol(s,t):
    def checkTreeIsIdentical(s,t):
            if not s and not t:
                return True

            if not s:
                return False

            if not t:
                return False

            if s.val != t.val:
                return False

            return checkTreeIsIdentical(s.right,t.right) and checkTreeIsIdentical(s.left,t.left)

        def traverse(s,t):
            if not s:
                return False
            else:
                if checkTreeIsIdentical(s,t):
                    return True
                else:
                    return traverse(s.right,t) or traverse(s.left,t)


        return  traverse(s,t)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def checkIfTreeIsIdentical(s,t):
            if s is None and t is None:
                return True
            if s is None:
                return False
            if t is None:
                return False
            if s.val != t.val:
                return False
            return checkIfTreeIsIdentical(s.left,t.left) and checkIfTreeIsIdentical(s.right,t.right)

        def traverse(n,n2):
            if checkIfTreeIsIdentical(n,n2):
                return True
            if n is not None:
                return traverse(n.left,n2) or traverse(n.right,n2)
            else:
                return False

        return traverse(s,t)
