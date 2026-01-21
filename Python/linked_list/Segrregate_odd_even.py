
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

    def segrregate_odd_even(self,head):
        if head is None or head.next is None:
            return head
        odd_head=Node(-1)
        even_head=Node(-1)
        odd_tail=odd_head
        even_tail=even_head

        temp=head
        while temp:
            if divmod(temp.data,2)[1]!=0:
                odd_tail.next=temp
                odd_tail=temp
            else:
                even_tail.next=temp
                even_tail=temp
            
            temp=temp.next
        odd_tail.next = None
        even_tail.next = odd_head.next
        return even_head.next
            
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

    head=sol.segrregate_odd_even(head)
    sol.printLL(head)

    