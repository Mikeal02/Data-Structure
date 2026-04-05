"""
DATE: April 5, 2026
PATTERN: Hashing, Boyer–Moore Extended (at most two candidates)

APPROACHES:
1. BRUTE FORCE:
- Step 1: Count frequency of each distinct element with full scans.
- TIME: O(n^2) | SPACE: O(1)

2. BETTER:
- Step 1: Hash map frequencies; pick elements with count > n/3.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Modified Boyer track up to two candidates with counters; verify counts.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: At most two values can appear more than n/3 times—track two running candidates.
"""

from collections import defaultdict


class Solution:
    # Brute force Approach: O(N^2)
    def majority_ele_by3(self,arr):
        n=len(arr)
        for i in range(n):
            count=0
            for j in range(n):
                if arr[i]==arr[j]:
                    count+=1

            if count>n//3:
                return arr[i]


    # Better Approach: O(n)
    def majority_ele_by3(self,arr):
        n=len(arr)
        freq=defaultdict(int)
        for i in range(n):
            freq[arr[i]]+=1

        for x,y in freq.items():
            if y>n//3:
                return x

    # optimal Approach: O(N)
    def majority_ele_by3(self,arr):
        n=len(arr)
        count1=0
        count2=0
        element_1=float("-inf")
        element_2=float("-inf")

        for x in arr:
            if count1==0 and element_2 !=x:
                count1+=1 
                element_1=x

            if count2==0 and element_1 !=x:
                count2+=1 
                element_2=x
                

            elif element_1==x:
                count1+=1

            elif element_2==x:
                count2+=1

            else:
                count1-=1
                count2-=1

        count1,count2=0,0
        if x in arr:
            if x==element_1:
                count1+=1

            if x==element_2:
                count2+=1

        if count1>n//3:
            return element_1

        if count2>n//3:
            return element_2
        


if __name__=="__main__":
    arr=[1,0,0,1,7,1,2,1,1]
    sol=Solution()
    ans=sol.majority_ele_by3(arr)
    print(f"The majority element with occurence greater than N/3 is {ans}")