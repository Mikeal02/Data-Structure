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

    # Iterative Approach: O(N)
    def reverseLL(self,head):
        temp=head
        prev=None
        while temp:
            curr=temp.next
            temp.next=prev
            prev=temp
            temp=curr
        return prev


    # recursive Approach:O(n)
    def reverseLL(self,head):
        if head is None or head.next is None:
            return head

        temp=head
        newhead=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newhead


    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        
        print()

if __name__=="__main__":
    sol=Solution()
    arr=list((1,3,4,5,6,7,3))
    head=sol.convert_arr_2LL(arr)

    print("LL Before Reversing:")
    sol.printLL(head)
    
    head=sol.reverseLL(head)
    print("LL after reversing:")
    sol.printLL(head)
        