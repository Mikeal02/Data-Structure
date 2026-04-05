"""
DATE: April 5, 2026
PATTERN: Linked List, Head Insert

APPROACHES:
1. BRUTE FORCE:
- Step 1: Rebuild entire list with new node at front from copied values.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Insert dummy head then move—same O(1) core.

3. OPTIMAL:
- Step 1: newNode.next = head; return newNode as new head.
- TIME: O(1) | SPACE: O(1)

AHA-MOMENT: Only the head pointer changes—no traversal for prepend on singly linked lists.
"""

from platform import node


class Node:
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    def insert_at_head(self,head,newData):
        newhead=Node(newData,head)
        return newhead

    def printList(self,head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next

if __name__=="__main__":
    sol=Solution()
    head=Node(2)
    head.next=Node(3)
    head.next.next=Node(4)

    print("Before Inserting")
    sol.printList(head)

    head=sol.insert_at_head(head,1)

    print("Before Inserting")
    sol.printList(head)

