"""
DATE: April 5, 2026
PATTERN: Linked List, Multi-precision Addition

APPROACHES:
1. BRUTE FORCE:
- Step 1: Convert both lists to big integers, add, split digits back.
- TIME: O(n) | SPACE: O(n) string/int storage

2. BETTER:
- Step 1: Push digits to stacks, pop while adding carry.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Reverse both lists, walk with carry, build dummy result, reverse output.
- TIME: O(n) | SPACE: O(1) besides output

AHA-MOMENT: Same as column addition—align least significant digits by reversing before merging.
"""

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Solution:

    def convert_arr_2LL(self, arr):
        head=Node(arr[0])
        prev=head
        for i in range(1,len(arr)):
            temp=Node(arr[i])
            prev.next=temp
            prev=temp
        return head

    def reverseLL(self,head):
        if head is None or head.next is None:
            return head
        new_head=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None

        return new_head


    def add_2LL(self,head1,head2):
        dummy_node=Node(-1)
        dummy_tail=dummy_node
        temp1=self.reverseLL(head1)
        temp2=self.reverseLL(head2)
        carry=0

        while (temp1 or temp2) or carry:
            sum_val=0
            if temp1 is not None:
                sum_val+=temp1.data
                temp1=temp1.next

            if temp2 is not None:
                sum_val+=temp2.data
                temp2=temp2.next

            sum_val+=carry
            carry=sum_val//10
            new_node=Node(sum_val%10)
            dummy_tail.next=new_node
            dummy_tail=dummy_tail.next
            
                
        return dummy_node.next


    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    arr1=list((2,4,3))
    arr2=list((5,6,7))
    head1=sol.convert_arr_2LL(arr1)
    head2=sol.convert_arr_2LL(arr2)
    sol.printLL(head1)
    sol.printLL(head2)
    ans=sol.add_2LL(head1,head2)
    sol.printLL(ans)