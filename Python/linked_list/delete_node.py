"""
DATE: April 5, 2026
PATTERN: Linked List Traversal

APPROACHES:
1. BRUTE FORCE:
- Step 1: Rebuild list from array excluding last value.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Count length then remove node at position length-1.
- TIME: O(n) | SPACE: O(1)

3. OPTIMAL:
- Step 1: Walk until temp.next.next is None; set temp.next=None (delete tail).
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Deleting last node only needs the penultimate node’s next pointer cleared.
"""

class Node:

    def __init__(self,val1,next1=None):
        self.val=val1
        self.next=next1

class Solution:
    # O(n),O(1)
    def delete_node(self,head):
        if head is None or head.next is None:
            return None

        temp=head
        while temp.next.next is not None:
            temp=temp.next;

        temp.next=None
        return head

    def printList(self,head):
        temp=head
        while temp:
            print(temp.val, end=" ")
            temp=temp.next

        print(end=" ")


if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)

    sol.printList(head)

    head=sol.delete_node(head)

    sol.printList(head)

    
        