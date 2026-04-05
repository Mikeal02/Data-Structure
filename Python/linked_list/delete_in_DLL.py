"""
DATE: April 5, 2026
PATTERN: Doubly Linked List, Deletion at Tail

APPROACHES:
1. BRUTE FORCE:
- Step 1: Copy list without last node into new list.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Find length, walk to node before last, null next.
- TIME: O(n) | SPACE: O(1)

3. OPTIMAL:
- Step 1: Walk to tail; set prev.next=None and clear back of removed node.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Tail delete in DLL is O(n) to reach tail—four pointer updates once at tail.
"""

class Node:
    def __init__(self,data1,next1=None,back1=None):
        self.data=data1
        self.next=next1
        self.back=back1

class Solution:
    def convert_arr_2DLL(self,arr):
        head=Node(arr[0])
        prev=head
        for i in range(1,len(arr)):
            temp=Node(arr[i],None,prev)
            prev.next=temp
            prev=temp

        return head

    def delete_in_DLL(self,head):
        if not head:
            return None

        if not head.next:
            return None

        temp=head
        while temp.next:
            temp=temp.next

        temp.back.next = None
        temp.back = None



    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        
        print()

if __name__=="__main__":
    sol=Solution()
    arr=list((1,3,4,5,6,7,3))
    head=sol.convert_arr_2DLL(arr)

    print("DLL Before Deleting:")
    sol.printLL(head)
    
    sol.delete_in_DLL(head)
    print("DLL after Deleting:")
    sol.printLL(head)
        