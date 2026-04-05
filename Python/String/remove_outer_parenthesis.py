"""
DATE: April 5, 2026
PATTERN: Balance / Depth Counter

APPROACHES:
1. BRUTE FORCE:
- Step 1: Parse full tree of primitives with recursion, drop outermost wrap each time.
- TIME: O(n) | SPACE: O(n) recursion

2. BETTER:
- Step 1: Stack-based matching to identify primitive blocks.

3. OPTIMAL:
- Step 1: Running depth; append '(' only when depth>0 before open; append ')' only when depth>0 after close.
- TIME: O(n) | SPACE: O(1) besides output

AHA-MOMENT: Outer parentheses are the times depth crosses from 0 to 1 and back—skip those characters.
"""

class Solution:
    # O(n)
    def remove_outer_parenthesis(self,s):
        result=""
        level=0
        for c in s:
            if c=='(':
                if level>0:
                    result+=c
                level+=1

            elif c==')':
                level-=1
                if level>0:
                    result+=c
                    
        return result

if __name__=="__main__":
    s="(()())(())"
    sol=Solution()
    result=sol.remove_outer_parenthesis(s)
    print(result)