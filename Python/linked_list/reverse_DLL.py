class Node:
    def __init__(self,data1,next1=None,back1=None):
        self.data=data1
        self.next=next1
        self.back=back1

class Solution:
    def convert_arr_2DLL(self,arr):
        head=Node(arr[0])
        prev=head
        for i in range(1,len(arr)):
            temp=Node(arr[i],None,prev)
            prev.next=temp
            prev=temp

        return head

    # Brute Force Approach: O(n),O(n)
    def reverse_DLL(self,head):
        temp=head
        stack=[]
        while temp:
            stack.append(temp.data)
            temp=temp.next

        temp=head
        while temp:
            temp.data=stack.pop()
            temp=temp.next

        return head

    # Optimal approach: O(n)
    def reverse_DLL(self,head):
        if head is None or head.next is None:
            return head
        temp=head
        while temp:
            curr=temp.next
            temp.next=temp.back
            temp.back=curr

            head=temp
            temp=curr

        return head



    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        
        print()

if __name__=="__main__":
    sol=Solution()
    arr=list((1,3,4,5,6,7,3))
    head=sol.convert_arr_2DLL(arr)

    print("DLL Before Reversing:")
    sol.printLL(head)
    
    head=sol.reverse_DLL(head)
    print("DLL after reversing:")
    sol.printLL(head)
        