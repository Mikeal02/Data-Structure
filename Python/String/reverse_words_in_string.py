"""
DATE: April 5, 2026
PATTERN: String Parsing, Reverse Iteration

APPROACHES:
1. BRUTE FORCE:
- Step 1: split(), reverse list, join.
- TIME: O(n) | SPACE: O(n) word list

2. BETTER:
- Step 1: Manual tokenize left-to-right into deque, pop from back when building.

3. OPTIMAL:
- Step 1: Scan string from right; skip spaces; capture each word boundary by index.
- TIME: O(n) | SPACE: O(n) for result string

AHA-MOMENT: Reversed word order is natural when reading the string from the end and peeling words.
"""

class Solution:
    # Optimal Solution: O(n)
    def reverse_words(self,s):
        n=len(s)
        result=""
        i=n-1
        while i>=0:
            while i>=0 and s[i]==' ':
                i-=1

            end=i
            while i>=0 and s[i]!=' ':
                i-=1;
            
            word=s[i+1:end+1]

            if result!="":
                result+=' '
            result+=word

        return result

if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverse_words(s))
