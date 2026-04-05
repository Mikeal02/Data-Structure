
"""
DATE: April 5, 2026
PATTERN: Floyd Cycle (phase 2: measure loop)

APPROACHES:
1. BRUTE FORCE:
- Step 1: Hash map of node to step index; on repeat return difference.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Store visited in set without timing—cannot get length directly.

3. OPTIMAL:
- Step 1: Detect meeting with slow/fast; fix one pointer at head, move both one step until meet (entry); count steps around cycle with fixed pointer.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: After collision, advancing one pointer to head and moving both equally finds cycle start; walk one loop to count length.
"""

class Node:
    # O(n),O(1)
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    # Brute Force Approach: O(n),O(n)
    # def length_of_loop(self,head):
    #     temp=head
    #     freq={}
    #     timer=0
    #     while temp:
    #         if temp in freq:
    #             return timer- freq[temp]
    #         else:
    #             freq[temp]=timer
    #         timer+=1
    #         temp=temp.next
    #     return 0

    # Optimal Approach:O(n)
    def length_of_loop(self,head):
        if head is None or head.next is None:
            return 0
        slow=head
        fast=head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        
        timer=1
        slow=slow.next
        while slow!=fast:
            slow=slow.next
            timer+=1

        return timer

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

    print(sol.length_of_loop(head))