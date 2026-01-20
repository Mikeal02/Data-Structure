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

    // Optimal Solution: O(n)
    int count_subarray_with_sumK(vector<int> &arr, int target)
    {
        unordered_map<int, int> freq;
        freq[0] = 1;  // empty prefix
    
        int current_sum = 0;
        int count = 0;
    
        for (int x : arr)
        {
            current_sum += x;
    
            if (freq.find(current_sum - target) != freq.end())
                count += freq[current_sum - target];
    
            freq[current_sum]++;
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