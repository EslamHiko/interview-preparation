'''
Problem Statement #
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

 head
  1
  2
  3
  4
  5
  6
 Cycle start
 Examples:
 Cycle start
  1
  2
  3
  4
  5
  6
  1
  2
  3
  4
  5
  6
 head
 head
 Cycle start
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
