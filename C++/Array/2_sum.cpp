#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    // brute force approach: O(n^2)
    string two_sum(vector<int>& arr,int target)
    {
        int n=arr.size();
        int current_sum=0;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                current_sum=arr[i]+arr[j];
                if(current_sum==target)
                {
                    return "YES";
                }
            }
        }
        return "NO";
    }

    // better approach 1:O(n),O(n)
    string two_sum(vector<int>& arr,int target)
    {
        unordered_map<int,int> mp;
        int n=arr.size();
        int remaining;
        for(int i=0;i<n;i++)
        {
            remaining=target-arr[i];
            if(mp.find(remaining)!=mp.end())
            {
                return "YES"
            }
            else{
                mp[arr[i]]=i;
            }
        }
        return "NO";
    }

    string two_sum(vector<int>& arr,int target)
    {
        int n=arr.size();
        sort(arr.begin(),arr.end());
        int left=0,right=n-1;
        while(left<right)
        {
            int current_sum=arr[left]+arr[right];
            if(current_sum<target)
            left++;

            else if(current_sum==target)
            {
                return "YES";
            }
            

            else
            right--;
        }
        return "NO";
    }

};

int main()
{
    vector<int>arr ={2,6,5,8,11};
    Solution sol;
    cout<<sol.two_sum(arr,12);
    return 0;
}