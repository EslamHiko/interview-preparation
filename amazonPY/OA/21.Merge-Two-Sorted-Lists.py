'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def sol(l1,l2):
    arr1 = []
    while l1:
        arr1.append(l1.val)
        l1 = l1.next
    arr2 = []
    while l2:
        arr2.append(l2.val)
        l2 = l2.next
    arr1 += arr2
    arr1.sort()
    if not len(arr1):
        return None
    x = ListNode(arr1[0])
    head = x
    for i in range(1,len(arr1)):
        x.next = ListNode(arr1[i])
        x = x.next
    return head
