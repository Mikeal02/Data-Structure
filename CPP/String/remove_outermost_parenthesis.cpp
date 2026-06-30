/*
 * DATE: April 5, 2026
 * PATTERN: Stack / Balance Counter, String Building
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Parse full primitive decomposition by recursive matching each balanced substring.
 * - TIME: O(n^2) naive splits | SPACE: O(n) recursion
 *
 * 2. BETTER:
 * - Step 1: Use stack of indices or characters to pop on match; strip outer when stack depth returns to 0 at end.
 * - TIME: O(n) | SPACE: O(n) stack
 *
 * 3. OPTIMAL:
 * - Step 1: Track nesting depth; on '(' increment—append only if depth>0 before increment; on ')' decrement before append if depth>0 after.
 * - TIME: O(n) | SPACE: O(1) besides output (depth is integer)
 *
 * AHA-MOMENT: Outer parentheses are exactly depth going 0→1 at start and 1→0 at end—skip those characters, keep inner levels.
 */

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    // O(N)
    string removeOuterParentheses(string arr)
    {
        string result="";
        int level=0;
        for(char c: arr)
        {
            if (c =='(')
            {
                if (level>0)
                {
                    result+=c;
                }
                level++;
            }
            else if (c==')')
            {
                level--;
                if(level>0)
                {
                    result+=c;
                }
            }
            
        }
        return result;
    }
};

int main() {
    string s = "(()())(())";  
    // Create object of Solution class
    Solution sol;             

    // Get result
    string ans = sol.removeOuterParentheses(s);

    // Print result
    cout << "The result is: " << ans << endl;

    return 0;
}