
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


    # Brute Force Approach: O(2*N),O(1)
    def sort_012(self,head):
        count_zero=0
        count_one=0
        count_two=0
        temp=head
        while temp:
            if temp.data==0:
                count_zero+=1
            elif temp.data==1:
                count_one+=1
            else:
                count_two+=1
            temp=temp.next
        
        temp=head
        while count_zero and temp is not None:
            temp.data=0
            count_zero-=1
            temp=temp.next

        while count_one and temp is not None:
            temp.data=1
            count_one-=1
            temp=temp.next

        while count_two and temp is not None:
            temp.data=2
            count_two-=1
            temp=temp.next
        
        return head

    # Optimal Solution: O(N)
    def sort_012(self,head):
        zero_head=Node(-1)
        one_head=Node(-1)
        two_head=Node(-1)
        zero_tail=zero_head
        one_tail=one_head
        two_tail=two_head

        temp=head
        while temp:
            next_node = temp.next  # Store the next node before modifying temp's next
            if temp.data==0:
                zero_tail.next=temp
                zero_tail=temp
                zero_tail.next = None  # Break the link
            elif temp.data==1:
                one_tail.next=temp
                one_tail=temp
                one_tail.next = None  # Break the link
            else:
                two_tail.next=temp
                two_tail=temp
                two_tail.next = None  # Break the link
            temp=next_node # Move to the next node in the original list

        zero_tail.next=one_head.next if one_head.next is not None else two_head.next
        one_tail.next=two_head.next if two_head.next is not None else None

        two_tail.next=None

        return zero_head.next


    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()




if __name__=="__main__":
    sol=Solution()
    arr=list((1,2,0,1,0,2))
    head=sol.convert_arr_2LL(arr)
    sol.printLL(head)
    head=sol.sort_012(head)
    sol.printLL(head)
