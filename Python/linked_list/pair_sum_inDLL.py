"""
DATE: April 5, 2026
PATTERN: Two Pointers on Sorted DLL

APPROACHES:
1. BRUTE FORCE:
- Step 1: Try all pairs (i,j) with i<j.
- TIME: O(n^2) | SPACE: O(1)

2. BETTER:
- Step 1: Hash complements for each left pointer—O(n) space.

3. OPTIMAL:
- Step 1: Left at head, right at tail; move inward by comparing sum to target (sorted order by value).
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Like two-sum on a sorted array—DLL gives O(1) move left and right via next/back.
"""

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

    def pairs_sum_DLL(self,head,target):
        if head is None:
            return []
        left=head
        right=head
        while right.next:
            right=right.next

        ans=[]
        while left and right and left.data < right.data:
            curr_sum=left.data+right.data

            if curr_sum==target:
                ans.append((left.data, right.data))
                left=left.next
                right=right.back

            elif curr_sum<target:
                left=left.next

            else:
                right=right.back


        return ans
        

    def printLL(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()


if __name__=="__main__":
    arr=list((3,4,6,2,1,9,11))
    sol=Solution()
    sort_arr=arr.sort()
    head=sol.convert_arr_2DLL(arr)
    print("Doubly Linked List Initially:")
    sol.printLL(head)
    

    pairs=sol.pairs_sum_DLL(head,10)
    print(pairs)