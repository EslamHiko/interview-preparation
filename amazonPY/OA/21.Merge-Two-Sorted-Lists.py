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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr = []
        while l1:
            arr.append(l1.val)
            l1 = l1.next
        while l2:
            arr.append(l2.val)
            l2 = l2.next

        arr.sort()
        if not len(arr):
            return
        head = ListNode(arr[0])
        temp = head
        for i in range(1,len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return head

# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

# recursively
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
