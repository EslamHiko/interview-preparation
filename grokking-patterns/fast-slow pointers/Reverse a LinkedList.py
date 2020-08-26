'''
Problem Statement #
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.

  2
  4
  6
  8
  10
  null
 Original List:
 Reversed List:
 Example:
  2
  4
  6
  8
  10
  null
 head
 head
Try it yourself #
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end= " ")
            temp = temp.next
        print()

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)

head.print_list()

def reverse(head):
    curr,prev,next = head,None,None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

reversed = reverse(head)
reversed.print_list()
