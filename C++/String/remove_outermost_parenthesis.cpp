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