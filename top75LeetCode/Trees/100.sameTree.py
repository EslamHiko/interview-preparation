'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''
def sol(p,q):
    def dfs(node1,node2):
        if node1 is None and node2 is None:
            return True
        if not node1:
            return False
        if not node2:
            return False
        if node1.val != node2.val:
            return False

        return dfs(node1.left,node2.left) and dfs(node1.right,node2.right)
    return dfs(p,q)
