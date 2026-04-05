"""
DATE: April 5, 2026
PATTERN: Doubly Linked List, Tail Insert

APPROACHES:
1. BRUTE FORCE:
- Step 1: Rebuild list with extra value at end.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Walk to tail, append—same as optimal without tail pointer.

3. OPTIMAL:
- Step 1: Traverse to last node; link next/back for new node.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Tail insert needs four link updates in a DLL—prev of new, next of old tail, etc.
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
    
    def insert_in_DLL(self,head,key):
        temp=head
        newnode=Node(key)
        if not head:
            return newnode

        while temp.next is not None:
            temp=temp.next

        temp.next=newnode
        newnode.back=temp

        return head

    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    arr=list((12,5,8,7,2,13,24,32))
    sol=Solution()

    head=sol.convert_arr_2DLL(arr)
    print("Doubly Linked List Initially:")
    sol.printLL(head)
    

    head=sol.insert_in_DLL(head,99)
    print("Doubly Linked List after inserting at tail:")
    sol.printLL(head)
