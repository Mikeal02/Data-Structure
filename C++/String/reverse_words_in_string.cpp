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