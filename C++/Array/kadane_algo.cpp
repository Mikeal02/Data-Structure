// Kadane Algorithm: Maximum Subarray Sum
#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    // Better Approach: O(n^2)
    int max_subarray_sum(vector<int>&arr)
    {
        int n=arr.size();
        int max_sum=INT_MIN;
        for(int i=0;i<n;i++)
        {
            int current_sum=0;
            for(int j=i;j<n;j++)
            {
                current_sum+=arr[j];
                max_sum=max(max_sum,current_sum);
            }
            
        }
        return max_sum;
    }

    // Optimal Approach: O(n) [Kadane's Algo]
    int max_subarray_sum(vector<int>&arr)
    {
        int n=arr.size();
        long long max_sum=LLONG_MIN;
        long long current_sum=0;
        for(int i=0;i<n;i++)
        {
            current_sum+=arr[i];
            if (current_sum<0)
            {
                current_sum=0;
            }
            max_sum=max(max_sum,current_sum);
        }
        return max_sum;
    }


    // Follow Up Question: Print the max_sum subarray
    int max_subarray_sum(vector<int>&arr)
    {
        int n=arr.size();
        long long max_sum=LLONG_MIN;
        long long current_sum=0;
        int start=0;
        int ansstart=-1,ansend=-1;

        for(int i=0;i<n;i++)
        {
            if(current_sum==0)
            {
                start=i;
            }
            current_sum+=arr[i];
            if(current_sum<0)current_sum=0;

            if(current_sum>max_sum)
            {
                max_sum=current_sum;
                ansstart=start;
                ansend=i;
            }

        }
        cout<<"[";
        for(int i=ansstart;i<=ansend;i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<"]";

        return max_sum;
    }

};

int main()
{
    vector<int> arr={2,3,5,-2,7,-4};
    Solution sol;
    int ans=sol.max_subarray_sum(arr);
    cout<<"The maximum subarray sum is "<<ans;
    return 0;
}