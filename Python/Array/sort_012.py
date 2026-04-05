"""
DATE: April 5, 2026
PATTERN: Dutch National Flag (Three-Way Partition)

APPROACHES:
1. BRUTE FORCE:
- Step 1: Use generic sort.
- TIME: O(n log n) | SPACE: O(log n)

2. BETTER:
- Step 1: Count 0s,1s,2s then overwrite array in three segments.
- TIME: O(n) | SPACE: O(1) counts, two passes

3. OPTIMAL:
- Step 1: Single-pass three pointers low/mid/high (DNF).
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Maintain four regions: <mid known, ==1, unknown, >high by swapping around mid.
"""

from itertools import count


class Solution:
    # brute force approach:O(n)
    def sort_012(self,arr):
        n=len(arr)
        count_zero,count_one,count_two=0,0,0
        for x in arr:
            if x==0:
                count_zero+=1
            elif x==1:
                count_one+=1
            else:
                count_two+=1
        
        index=0
        while count_zero>0:
            arr[index]=0
            index+=1
            count_zero-=1
            
        while count_one>0:
            arr[index]=1
            index+=1
            count_one-=1

        while count_two>0:
            arr[index]=2
            index+=1
            count_two-=1

    # Optimal approach:O(n)
    def sort_012(self,arr):
        n=len(arr)
        low,mid,high=0,0,n-1
        while mid<=high:
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1

            elif arr[mid]==1:
                mid+=1

            else:
                arr[high],arr[mid]=arr[mid],arr[high]
                high-=1

if __name__=="__main__":
    arr=[2,0,2,1,1,2]
    sol=Solution()
    sol.sort_012(arr)
    print(arr)