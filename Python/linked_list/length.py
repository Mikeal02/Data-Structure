
class Node:
    # O(n),O(1)
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    def length_LL(self,head):
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next

        return length

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)

    ans=sol.length_LL(head)
    print(f"The length of LL is {ans}")