#include<bits/stdc++.h>
using namespace std;

class Solution
{
    // brute force approach:O(n^3)
    int longest_subarray_k(vector<int> &arr,int k)
    {
        int n=arr.size();
        int maxi=0;
        for(int i=0;i<n;i++)
        {
            for(int j=i;j<n;j++)
            {
                int current_sum=0;
                for(int k=i;k<=j;k++)
                {
                    current_sum+=arr[k];
                
                if(current_sum==k)
                {
                     max_sub_len=max(maxi,j-i+1);
                }
                }
            }
        }
        return max_sub_len;
    }

    // Optimal Approach: O(n) [Using SLiding window Algorithm]
    int longest_subarray_k(vector<int> &arr,int k)
    {
        int n=arr.size();
        int left=0,right=0;
        int current_sum=arr[0];
        int max_sub_len=0;
        while(right<n)
        {
            while(left<=right && current_sum>k)
            {
                current_sum-=arr[left];
                left++;
            }
            if(current_sum==k)
            {
                max_sub_len=max(max_sub_len,right-left+1);
            }
            right++;
            if(right<n)
            {
                current_sum+=arr[right];
            }
        }
        return max_sub_len;
        
    }
};

int main()
{
    Solution sol;
    vector<int> arr={10,5,2,7,1,9};
    int k;
    cin>>k;
    int ans=sol.longest_subarray_k(arr,k);
    cout<<"The longest Subarray with Sum "<<k<<"is "<<ans;
    return 0;

}