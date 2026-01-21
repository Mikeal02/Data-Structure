
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

    # Brute Force Approach:O(l1*l2)
    def intersection_YLL(self,head1,head2):
        while head2:
            temp=head1
            while temp:
                if temp==head2:
                    return head2
                temp=temp.next

            head2=head2.next

        return None


    # Better Approach 1: O(N1+N2),O(N1)
    def intersection_YLL(self,head1,head2):
        temp=head1
        freq={}
        while temp:
            freq[temp]=1
            temp=temp.next


        temp=head2
        while temp:
            if temp in freq:
                return temp.data

            temp=temp.next
        return None

    # Optimal Approach 1: O(2*max(l1,l2)+O(abs(l1-l2))),O(1)
    def intersection_YLL(self, head1, head2):
        length1 = length2 = 0
        temp = head1
        while temp:
            length1 += 1
            temp = temp.next

        temp = head2
        while temp:
            length2 += 1
            temp = temp.next

        diff = length1 - length2
    
        if diff > 0:
            while diff:
                head1 = head1.next
                diff -= 1
        else:
            while diff:
                head2 = head2.next
                diff += 1

        while head1 and head2:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next

        return None

    # Optimal Approach 2:

    def intersection_YLL(self,head1,head2):
        temp1=head1
        temp2=head2

        while temp1 and temp2:
            if temp1==temp2:
                return temp1

            if temp1.next is None:
                temp1=head2
            
            if temp2.next is None:
                temp2=head1
            temp1=temp1.next
            temp2=temp2.next
        return None




    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    arr1=list((1,3,1,2,4))
    arr2=list((3,2,4))
    head1=sol.convert_arr_2LL(arr1)
    head2=sol.convert_arr_2LL(arr2)
    sol.printLL(head1)
    sol.printLL(head2)
    ans=sol.intersection_YLL(head1,head2)
    print(f"The intersection point is {ans.data}")