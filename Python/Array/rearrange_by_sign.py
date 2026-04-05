"""
DATE: April 5, 2026
PATTERN: Two-Phase Array Construction

APPROACHES:
1. BRUTE FORCE:
- Step 1: Split positives and negatives then interleave by index rules.
- TIME: O(n) | SPACE: O(n)

2. BETTER:
- Step 1: Write to answer array with separate even/odd index pointers for signs.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Same asymptotics; in-place alternating variants exist for specific constraints.
- TIME: O(n) | SPACE: O(n) for output buffer in typical solution

AHA-MOMENT: Separate “collect by sign” from “place at alternating slots” to keep indices simple.
"""

from operator import ne, neg


class Solution:
    # Brute Force approach: O(n+n/2),O(n)
    # def arrange_by_sign(self,arr):
    #     n=len(arr)
    #     positive=[]
    #     negative=[]
    #     for x in arr:
    #         if x>0:
    #             positive.append(x)
    #         else:
    #             negative.append(x)


    #     for i in range(n//2):
    #         arr[2*i]=positive[i]
    #         arr[2*i+1]=negative[i]

    #     return arr

    # Optimal Approach: O(n),O(n)
    def arrange_by_sign(self,arr):
        n=len(arr)
        ans=[0]*n
        pos_index=0
        neg_index=1
        for x in arr:
            if x>0:
                ans[pos_index]=x
                pos_index+=2
            else:
                ans[neg_index]=x
                neg_index+=2

        return ans


if __name__=="__main__":
    arr=[2,4,-6,7,-9,1,-5,-11,12,-17]
    sol=Solution()
    ans=sol.arrange_by_sign(arr)
    print(ans)