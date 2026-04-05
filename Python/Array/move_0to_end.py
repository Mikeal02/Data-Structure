"""
DATE: April 5, 2026
PATTERN: Two Pointers, Partition

APPROACHES:
1. BRUTE FORCE:
- Step 1: Build new list without zeros then pad zeros.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Stable partition using extra array of same size.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: In-place: write non-zeros forward with slow pointer, or swap non-zero forward.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Treat zeros as holes to fill—compact non-zeros to the front.
"""

class Solution:
    # brute force approach: O(2n),O(n)
    def move_zero_to_end(self,arr):
        temp=[]
        for i in range(len(arr)):
            if arr[i]!=0:
                temp.append(arr[i])

        zeros=len(arr)-len(temp)
        temp.extend([0]*zeros)


        for i in range(len(arr)):
            arr[i]=temp[i]

        return arr
        
    # Optimal Approach:O(n)
     def move_zero_to_end(self,arr):
        for i in range(len(arr)):
            if arr[i]==0:
                j=i
                break

        for i in range(j+1,len(arr)):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        
        return arr

if __name__=="__main__":
    arr=[1,0,23,2,0,0,4,5,1]
    sol=Solution()
    sol.move_zero_to_end(arr)
    print(arr)
