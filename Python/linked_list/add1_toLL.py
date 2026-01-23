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

    # Iterative Approach: O(N)
    def add1_toLL(self,head):
        temp=self.reverseLL(head)
        dummy_node=Node(-1)
        dummy_tail=dummy_node
        carry=1
        while temp or carry:
            sum_val = carry
            if temp:
                sum_val += temp.data
                temp = temp.next
            carry = sum_val // 10
            new_node = Node(sum_val % 10)
            dummy_tail.next=new_node
            dummy_tail=dummy_tail.next

        temp2=self.reverseLL(dummy_node.next)
        return temp2

    # Recursive Approach:
    def add1_toLL(self,head):
        if not head:
            return 1

        carry=self.add1_toLL(head.next)
        sum_val=head.data+carry
        head.data=sum_val%10
        return sum_val//10


    def reverseLL(self,head):
        if head is None or head.next is None:
            return head
        new_head=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None

        return new_head

    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    arr1=list((9,9,9))
    head1=sol.convert_arr_2LL(arr1)
    sol.printLL(head1)
    ans=sol.add1_toLL(head1)
    sol.printLL(ans)