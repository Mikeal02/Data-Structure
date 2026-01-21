class Node:
    # O(n),O(1)
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    def convert_arr_2LL(self, arr):
        head=Node(arr[0])
        prev=head
        for i in range(1,len(arr)):
            temp=Node(arr[i])
            prev.next=temp
            prev=temp
        return head

    # Brute Force Approach:O(n+n/2)
    def middle_of_LL(self,head):
        if not head:
            return -1

        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        
        mid_node=length//2
        temp=head
        while temp:
            if mid_node==0:
                break
            temp=temp.next
            mid_node-=1

        return temp.data

    # Optimal Approach: O(n/2),O(1)
    def middle_of_LL(self,head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

        return slow.data

    
if __name__=="__main__":
    arr=list((2,3,4,5,6,7,8,1,2))
    sol=Solution()
    head=sol.convert_arr_2LL(arr)
    ans=sol.middle_of_LL(head)
    print(f"The middle node value is {ans}")