
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

    # Brute force Approach: O(n),O(n)
    def is_palindrome(self,head):
        temp=head
        stack=[]
        while temp:
            stack.append(temp.data)
            temp=temp.next

        temp=head
        while temp:
            if temp.data!=stack.pop():
                return False
            temp=temp.next
        return True

    def is_palindrome(self,head):
        if head is None or head.next is None:
            return True
        slow=head
        fast=head

        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next

        newhead=self.reverseLL(slow.next)
        first=head
        second=newhead

        while second is not None:
            if first.data!=second.data:
                return False
            first=first.next
            second=second.next
        return True


    def reverseLL(self,head):
        if head is None or head.next is None:
            return head
        newhead=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newhead

    
if __name__=="__main__":
    sol=Solution()
    arr=list((1,3,4,5,6,4,3,1))
    head=sol.convert_arr_2LL(arr)

    if sol.is_palindrome(head):
        print(f"Yes, LL is Palindrome:")
    else:
         print(f"NO, LL is not Palindrome:")
