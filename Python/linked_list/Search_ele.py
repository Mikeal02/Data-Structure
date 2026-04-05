"""
DATE: April 5, 2026
PATTERN: Linear Search on Linked List

APPROACHES:
1. BRUTE FORCE:
- Step 1: Recursive search returning index—extra stack.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Same linear scan with index counter.

3. OPTIMAL:
- Step 1: Iterative walk; return index when data matches else continue.
- TIME: O(n) worst | SPACE: O(1)

AHA-MOMENT: Linked lists have no random access—search is inherently linear.
"""

class Node:
    # O(n),O(1)
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    # O(n),O(1)
    def search_element(self,head,key):
        temp=head
        index=0

        while temp:
            if temp.data==key:
                return index
            else:
                temp=temp.next
                index+=1

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)

    print(f"Index is {sol.search_element(head,4)}")