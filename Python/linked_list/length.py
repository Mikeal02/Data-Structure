"""
DATE: April 5, 2026
PATTERN: Linked List Traversal

APPROACHES:
1. BRUTE FORCE:
- Step 1: Copy nodes to list and use len().
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Recursive length with stack.
- TIME: O(n) | SPACE: O(n) stack

3. OPTIMAL:
- Step 1: Iterative walk with counter until None.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Length is the number of next hops to null—one pass, one counter.
"""

class Node:
    # O(n),O(1)
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    def length_LL(self,head):
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next

        return length

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)

    ans=sol.length_LL(head)
    print(f"The length of LL is {ans}")