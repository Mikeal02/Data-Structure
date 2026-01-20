#include<bits/stdc++.h>
using namespace std;
 
class Solution
{
    public:
    // Brute Force approach: O(n+n/2),O(n)
    void rearrange_by_sign(vector<int>& arr)
    {
        int n=arr.size();
        vector<int> positive;
        vector<int> negative;
        for(int x:arr)
        {
            if(x>0)positive.push_back(x);
            else negative.push_back(x);
        }
        int index=0;
        for(int i=0;i<n/2;i++)
        {
            arr[2*i]=positive[i];
            arr[2*i+1]=negative[i];
        }
        
    }

    // Optimal Approach:O(n)
    void rearrange_by_sign(vector<int>& arr)
    {
        int n=arr.size();
        vector<int>ans(n,0);
        int pos_index=0,neg_index=1;
        for(int i=0;i<n;i++)
        {
            if(arr[i]<0)
            {
                ans[neg_index]=arr[i];
                neg_index+=2;
            }
            else
            {
                ans[pos_index]=arr[i];
                pos_index+=2;
            }
        }
       
};

int main()
{
    vector<int> arr={2,4,-6,7,-9,1,-5,-11,12,-17};
    Solution sol;
    sol.rearrange_by_sign(arr);
    for(int x:arr)
    {
        cout<<x<<" ";
    }
    return 0;
}