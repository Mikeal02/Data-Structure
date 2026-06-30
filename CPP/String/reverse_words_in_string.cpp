/*
 * DATE: April 5, 2026
 * PATTERN: String Parsing, Two Pointers
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Split by spaces into vector of words (manual or stream), reverse vector, join.
 * - TIME: O(n) | SPACE: O(n) for words storage
 *
 * 2. BETTER:
 * - Step 1: Single pass collect words, build answer from end word to start with spaces.
 * - TIME: O(n) | SPACE: O(n)
 *
 * 3. OPTIMAL (in-place variant exists on char arrays):
 * - Step 1: Trim/skip spaces; scan from right, identify word boundaries, append words to result.
 * - TIME: O(n) | SPACE: O(n) for output string
 *
 * AHA-MOMENT: Word order reversal is easier when scanning the string from the right—each word is a contiguous non-space run.
 */

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    // Brute Force Approach: O(n),O(n)
    string reverse_words(string s)
    {
        int n=s.length();
        vector<string> words;
        int start,end;
        int i=0;
        while(i<n)
        {
            if(i<n && s[i]==' ')i++;
            start=i;

            while(i<n && s[i]!=' ')i++;
            end=i-1;

            string wordfound=s.substr(start,end-start+1);
            words.push_back(wordfound);
            
        }
        string ans="";
        for(i=words.size()-1;i>=0;i--)
        {
            ans+=words[i];
            if(i!=0)ans.push_back(' ');

        }
        return ans;
    }

    // Optimal Approach:
    string reverse_words(string s)
    {
        string result="";
        int n=s.length();
        int i=n-1;
        while(i>=0)
        {
            while(i>=0 && s[i]==' ')i--;
            if(i<0)break;

            int end=i;
            while(i>=0 && s[i]!=' ')i--;

            string word=s.substr(i+1,end-i);

            if(!result.empty())
            {
                result+=" ";
            }
            result+=word;
        }
        return result;
    }
};

int main(){
    string s =  " amazing coding skills ";
    
    // Creating an instance of Solution class
    Solution sol; 
    
    // Function call to reverse every word in the given string
    string ans = sol.reverse_words(s);
    
    // Output
    cout << "Input string: " << s << endl;
    cout << "After reversing every word: " << ans << endl;
    return 0;
}