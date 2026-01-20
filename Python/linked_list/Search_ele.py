class Node:
    # O(n),O(1)
    def __init__(self,data1,next1=None):
        self.data=data1
        self.next=next1

class Solution:
    def search_element(self,head,key):
        temp=head
        index=0

        while temp:
            if temp.data==key:
                return index
            else:
                temp=temp.next
                index+=1

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)

    print(f"Index is {sol.search_element(head,4)}")