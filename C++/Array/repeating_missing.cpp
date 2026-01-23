#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    vector<int> repeating_missing(vector<int> &arr)
    {
        int n=arr.size();
        vector<int> hash(n+1,0);
        vector<int>ans;
        for(int i=0;i<n;i++)
        {
            hash[arr[i]]++;
        }
        for(int i=0;i<hash.size();i++)
        {
            if(hash[i]==2)
            {
                ans.push_back(i);
            }
            if(hash[i]==0)
            {
                ans.push_back(i);
            }
        }
        return ans;
    }
};

int main() {
    vector<int> nums = {3, 1, 2, 5, 4, 6, 7, 5};
    
    // Create an instance of Solution class
    Solution sol;

    vector<int> result = sol.repeating_missing(nums);
    
    // Print the repeating and missing numbers found
    cout << "The repeating and missing numbers are: {" << result[0] << ", " << result[1] << "}\n";
    
    return 0;
}