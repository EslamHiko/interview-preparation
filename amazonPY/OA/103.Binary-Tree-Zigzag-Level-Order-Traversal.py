'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

def sol(root):
    if not root:
        return []
    queue=[]
    queue.append(root)
    res=list()
    neg = 1
    while len(queue):
        nextbatch=list()
        if neg == -1:
            res.append([i.val for i in queue[::-1] if i is not None])
        else:
            res.append([i.val for i in queue if i is not None])
        neg = neg*(-1)
        for i in queue:
            if i:
                if i.left:
                    nextbatch.append(i.left)
                if i.right:
                    nextbatch.append(i.right)
        queue=nextbatch
    return res
