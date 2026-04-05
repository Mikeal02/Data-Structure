/*
 * DATE: April 5, 2026
 * PATTERN: Dynamic Programming (running state), Array
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Enumerate every subarray (i..j) and compute sum.
 * - Step 2: Track global maximum sum.
 * - TIME: O(n^3) naive or O(n^2) with running inner sum | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Prefix sums: max subarray ending at j is max over i of (P[j]-P[i-1]) in O(n^2).
 * - TIME: O(n^2) | SPACE: O(n) for prefix array
 *
 * 3. OPTIMAL (Kadane):
 * - Step 1: Track current_sum; reset or extend: if current_sum + arr[i] is best, extend; optionally reset negative running sum to 0 (all-negative arrays need tracking max element separately).
 * - Step 2: Update global max each step.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Optimal subarray ending at i either extends the best ending at i-1 or starts fresh at i—constant state suffices.
 */

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