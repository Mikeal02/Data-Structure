"""
DATE: April 5, 2026
PATTERN: Greedy, String Scan

APPROACHES:
1. BRUTE FORCE:
- Step 1: Try every substring ending at each position, check odd numeric value.
- TIME: O(n^3) with conversion | SPACE: O(n)

2. BETTER:
- Step 1: From right, find last odd digit; take prefix from first non-leading zero to that digit.
- TIME: O(n) | SPACE: O(1) extra

3. OPTIMAL:
- Step 1: Same single right-to-left scan for last odd; trim leading zeros on left bound.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Larger magnitude means longer prefix with a valid odd last digit—scan from the right for the last odd digit.
"""

class Solution:
    # O(n)
    def largest_odd_number(self,s:str)->str:
        ind=-1

        i=0
        for i in range(len(s)-1,-1,-1):
            if(int(s[i])%2)==1:
                ind=i
                break

        i=0
        while i<=ind and s[i]=='0':
            i+=1

        return s[i:ind+1]

if __name__=="__main__":
    solution = Solution()
    num = "0214638"

    result = solution.largest_odd_number(num)
    print("Largest odd number:", result)