"""
DATE: April 5, 2026
PATTERN: Sorting + Two Pointers (k-Sum / 4Sum)

APPROACHES:
1. BRUTE FORCE:
- Step 1: Try all quadruples (i,j,k,l) and compare sum to target.
- TIME: O(n^4) | SPACE: O(1)

2. BETTER:
- Step 1: Hash pair sums—still heavy on memory.
- TIME: O(n^2) to O(n^3) variants | SPACE: O(n^2) possible

3. OPTIMAL:
- Step 1: Sort; fix i,j then two-pointer on remaining range; skip duplicates.
- TIME: O(n^3) | SPACE: O(1) besides output lists

AHA-MOMENT: Reducing two free indices to a sorted two-pointer sweep cuts one layer of brute force.
"""

class Solution:
    def fourSum(self, arr, target):
        n=len(arr)
        arr.sort()
        ans=[]

        for i in range(n):
            if i>0 and arr[i]==arr[i-1]:
                continue

            for j in range(i + 1, n):
                if j>i+1 and arr[j]==arr[j-1]:
                    continue

                left, right=j+1,n-1
                while left<right:
                    total=arr[i]+arr[left]+arr[right]
                    if total==target:
                        ans.append([arr[i],arr[j],arr[left],arr[right]])
                        while left<right and arr[left]==arr[left+1]:
                            left+=1
                        while left<right and arr[right]==arr[right-1]:
                            right-=1
                        left+=1
                        right-=1

                    elif total<target:
                        left+=1
                    else:
                        right-=1

        return ans

arr=[1,0,-1,0,-2,2]
target=0
obj=Solution()
print(obj.fourSum(arr,target))
