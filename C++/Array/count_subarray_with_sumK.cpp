#include<bits/stdc++.h>
using namespace std;
 
class Solution
{
    public:
    // Brute Force Approach: O(n^2)
    int count_subarray_with_sumK(vector<int> & arr,int target)
    {
        int n=arr.size();
        int count=0;
        for(int i=0;i<n;i++)
        {
            int current_sum=0;
            for(int j=i;j<n;j++)
            {
                current_sum+=arr[j];
                if(current_sum==target)count++;
            }

        }
        return count;
    }

    int count_subarray_with_sumK(vector<int> & arr,int target)
    {
        int n=arr.size();
        int count=0;
        int left=0,right=0;
        int current_sum=arr[0];
        while(right<n)
        {
            c
            while(left<right && current_sum>k)
            {
                current_sum-=arr[left];
                left++;
            }
            if(current_sum==target)count++;
            right++;
            if(right<n)
            {
                current_sum+=arr[right];
            }

        }
        return count;
    }
};

int main()
{
    vector<int>arr={3,1,2,4};
    Solution sol;
    int ans=sol.count_subarray_with_sumK(arr,k);
    cout<<"The number of subarray with sum K is "<<ans;
    return 0;
}