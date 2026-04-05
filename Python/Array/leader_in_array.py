"""
DATE: April 5, 2026
PATTERN: Suffix Maximum / Greedy Right-to-Left

APPROACHES:
1. BRUTE FORCE:
- Step 1: For each i, scan right for any larger element.
- TIME: O(n^2) | SPACE: O(n) for answer

2. BETTER:
- Step 1: Precompute suffix max array.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Walk from right; track max from right; leaders when arr[i] > max_so_far (variant by definition).
- TIME: O(n) | SPACE: O(1) extra

AHA-MOMENT: A leader is larger than everything to its right—suffix scan carries exactly that information.
"""

class Solution:
    # Brute force approach: O(n^2)
    def leader_in_array(self,arr):
        n=len(arr)
        ans=[]
        for i in range(len(n)-1):
            leader=True
            for j in range(i+1,len(n)):
                if arr[j]>arr[i]:
                    leader=False
                    break
            
            if leader==True:
                ans.append(arr[i])

        ans.append(arr[n-1])
        return ans

                



    # Optimal Approach: O(n)
    def leader_in_array(self,arr):
        n=len(arr)
        ans=[]
        max_element=arr[-1]
        ans.append(arr[-1])
        for i in range(n-2,-1,-1):
            if arr[i]>max_element:
                ans.append(arr[i])
                max_element=arr[i]

        ans.reverse()
        return ans

if __name__=="__main__":
    arr=[10,22,12,3,0,6]
    sol=Solution()
    ans=sol.leader_in_array(arr)
    print(ans)
