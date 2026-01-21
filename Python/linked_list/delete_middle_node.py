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
    # Brute Force Approach: O(L+L/2)
    def delete_middle_node(self,head):
        if head is None or head.next is None:
            return head
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next

        index=length//2-1
        temp=head
        while index:
            temp=temp.next
            index-=1

        middle_node=temp.next
        temp.next=temp.next.next
        del middle_node
        return head
    
    # Optimal Approach:O(L/2)
    def delete_middle_node(self,head):
        if head is None or head.next is None:
            return head
        slow=head
        fast=head.next
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

        middle_node=slow.next
        slow.next=slow.next.next
        del middle_node
        return head



    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()


if __name__=="__main__":
    sol=Solution()
    arr=list((1,2,4,6,8,3))
    head=sol.convert_arr_2LL(arr)
    sol.printLL(head)
    head=sol.delete_middle_node(head)
    sol.printLL(head)

    