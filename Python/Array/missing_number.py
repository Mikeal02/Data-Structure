"""
DATE: April 5, 2026
PATTERN: Sum Formula, XOR

APPROACHES:
1. BRUTE FORCE:
- Step 1: For each number 1..N check membership in arr.
- TIME: O(N^2) | SPACE: O(1)

2. BETTER:
- Step 1: Set of arr elements; find missing in 1..N.
- TIME: O(N) | SPACE: O(N)

3. OPTIMAL:
- Step 1: Expected sum N(N+1)/2 minus actual sum, or XOR all indices and values.
- TIME: O(N) | SPACE: O(1)

AHA-MOMENT: XOR cancels pairs; missing number is the XOR residue (or use sum difference).
"""

from operator import xor


class solution:
    # brute force: O(N^2)
    # def missing_num(self,arr,N):
    #     for i in range(1,N+1):
    #         if i not in arr:
    #             return i
    #
    # # Optimal 1: O(n),O(1)
    #
    # def missing_num(self,arr,N):
    #     sum1=(N*(N+1)/2)
    #     for i in arr:
    #         sum2+=i
    #
    #     return sum1-sum2

    # Optimal 2:O(N)
    def missing_num(self,arr,N):
        xor1,xor2=0,0
        for i in range(1,N+1):
            xor1^=i
        
        for i in arr:
            xor2^=i
        
        return xor1^xor2
        




if __name__=="__main__":
    arr=list((1,2,3,4,5,7))
    sol=solution()
    
    print(f"The missing number is {sol.missing_num(arr,7)}")