"""
DATE: April 5, 2026
PATTERN: Floyd Cycle Detection, Hashing

APPROACHES:
1. BRUTE FORCE:
- Step 1: For each node, compare with all previous nodes’ addresses.
- TIME: O(n^2) | SPACE: O(1)

2. BETTER:
- Step 1: Hash set of visited nodes; cycle if revisit.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Tortoise and hare—if fast meets slow, cycle exists.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Two speeds guarantee meeting inside a cycle; no extra memory needed.
"""

class Node:
    # O(n),O(1)
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    # Brute Force Approach: O(n),O(n)
    def detect_loop(self,head):
        temp=head
        freq={}
        while temp:
            if temp in freq:
                return True
            else:
                freq[temp]=1
            temp=temp.next
        return False

    # Optimal Approach:O(n)
    def detect_loop(self,head):
        if head is None or head.next is None:
            return False
        slow=head
        fast=head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
            
        return False

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    fifth=Node(5)

    head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth
    fifth.next=third

    print(sol.detect_loop(head))