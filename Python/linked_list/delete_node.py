class Node:

    def __init__(self,val1,next1=None):
        self.val=val1
        self.next=next1

class Solution:
    # O(n),O(1)
    def delete_node(self,head):
        if head is None or head.next is None:
            return None

        temp=head
        while temp.next.next is not None:
            temp=temp.next;

        temp.next=None
        return head

    def printList(self,head):
        temp=head
        while temp:
            print(temp.val, end=" ")
            temp=temp.next

        print(end=" ")


if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)

    sol.printList(head)

    head=sol.delete_node(head)

    sol.printList(head)

    
        