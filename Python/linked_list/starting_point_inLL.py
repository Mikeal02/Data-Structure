
"""
DATE: April 5, 2026
PATTERN: Floyd Cycle (entry point)

APPROACHES:
1. BRUTE FORCE:
- Step 1: Hash visited nodes; first repeat is start of cycle.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Store timestamps per node.

3. OPTIMAL:
- Step 1: Meet slow/fast inside cycle; reset one to head; move both one step until they meet at entry.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Distance from head to cycle entry equals distance from meeting point to entry along the cycle—Floyd’s phase 2.
"""

class Node:
    # O(n),O(1)
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    # Brute Force Approach: O(n),O(n)
    def starting_point_LL(self,head):
        temp=head
        freq={}
        while temp:
            if temp in freq:
                return temp.data
            else:
                freq[temp]=1
            temp=temp.next
        return None

    # Optimal Approach:O(n)
    def starting_point_LL(self,head):
        if head is None or head.next is None:
            return head
        slow=head
        fast=head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
            if slow==fast:
                return slow.data
                
        return None

        

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
    fifth.next=fourth

    print(sol.starting_point_LL(head))