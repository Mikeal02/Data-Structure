"""
DATE: April 5, 2026
PATTERN: Prefix Sum, Hash Map

APPROACHES:
1. BRUTE FORCE:
- Step 1: Enumerate all subarrays and compare sum to K.
- TIME: O(n^2) | SPACE: O(1)

2. BETTER:
- Step 1: Prefix array without hashing; still O(n^2) pairs.
- TIME: O(n^2) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Running prefix sum with frequency map; add freq[prefix - K]; freq[0]=1.
- TIME: O(n) | SPACE: O(n)

AHA-MOMENT: Count of valid subarrays ending at i equals number of earlier prefixes equal to current_prefix - K.
"""

class Solution:
    # Brute Force Approach: O(n^2)
    def count_subarray_with_sumk(self,arr,target):
        n=len(arr)
        count=0
        
        for i in range(n):
            current_sum=0
            for j in range(i,n):
                current_sum+=arr[j]
                if current_sum==target:
                    count+=1
                    
        return count
    
    # Optimal Solution: O(n)
    def count_subarray_with_sumk(self,arr,target):
        n=len(arr)
        count=0
        freq={}
        freq[0]=1
        current_sum=0
        for i in range(n):
            current_sum+=arr[i]
            remove=current_sum-target
            if (remove) in freq:
                count+=freq[(remove)]

            
            freq[current_sum]=freq.get(current_sum,0)+1
        return count

    

if __name__=="__main__":
    arr=[2,3,1,4]
    sol=Solution()
    k=5
    ans=sol.count_subarray_with_sumk(arr,k)
    print(f"The number of subarray with sum k is {ans}")