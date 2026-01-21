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

    # Brute Force Approach:O(l)+O(L-N),O(1)
    def remove_nth_fromend(self,head,N):
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next

        index=length-N-1
        temp=head
        while index>0:
            temp=temp.next
            index-=1
        
        nth_node=temp.next
        temp.next=temp.next.next
        del nth_node
        return head

    # Optimal Approach:O(L)
    def remove_nth_fromend(self,head,N):
        slow=head
        fast=head
        while N>0:
            fast=fast.next
            N-=1
        
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next

        nth_node=slow.next
        slow.next=slow.next.next
        del nth_node
        return head

    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

    
if __name__=="__main__":
    sol=Solution()
    arr=list((1,2,4,6,8,3,9,11,18))
    head=sol.convert_arr_2LL(arr)
    sol.printLL(head)
    head=sol.remove_nth_fromend(head,5)
    sol.printLL(head)

    