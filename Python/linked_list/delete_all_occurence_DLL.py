"""
DATE: April 5, 2026
PATTERN: Doubly Linked List, Multi-Deletion

APPROACHES:
1. BRUTE FORCE:
- Step 1: Build new list excluding key by scanning into new structure.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Mark nodes to delete then second pass—still two passes.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Single pass; when data==key, relink prev.next and next.back; advance using saved next pointer.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Save next before mutating links—otherwise you lose the traversal cursor when deleting current.
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

    def delete_all_occurence(self, head, key):
        temp = head

        while temp:
            next_node = temp.next  # save next before deletion

            if temp.data == key:
            # if deleting head
                if temp.back is None:
                    head = temp.next
                    if head:
                        head.back = None
                else:
                    temp.back.next = temp.next
                    if temp.next:
                        temp.next.back = temp.back

                del temp  # optional in Python, but fine

            temp = next_node

        return head


    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()


if __name__=="__main__":
    arr=list((1,8,12,5,6,12,12))
    sol=Solution()

    head=sol.convert_arr_2DLL(arr)
    print("Doubly Linked List Initially:")
    sol.printLL(head)
    

    head=sol.delete_all_occurence(head,12)
    print("Doubly Linked List after deleting all occurence:")
    sol.printLL(head)
