/*
 * DATE: April 5, 2026
 * PATTERN: Prefix Sum, Hashing, Sliding Window
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Enumerate all subarrays (i..j) and compute each sum.
 * - Step 2: Track maximum length where sum equals K.
 * - TIME: O(n^3) with naive resum, or O(n^2) with running sum inner loop | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Use prefix sums P[j] - P[i-1] to get any subarray sum in O(1) after O(n) prefix build.
 * - Step 2: Still need pairs (i,j) without extra structure—often O(n^2).
 * - TIME: O(n^2) | SPACE: O(n) for prefix array
 *
 * 3. OPTIMAL:
 * - Step 1 (general integers): For each end index, need earlier prefix equal to (current_prefix - K); track first index of each prefix in a map for longest length.
 * - Step 2 (non-negative array only): Sliding window shrink when sum > K.
 * - TIME: O(n) | SPACE: O(n) for hash map (window is O(1) extra)
 *
 * AHA-MOMENT: Longest length with sum K is a “first occurrence of prefix” problem: length = i - firstIndex[prefix - K].
 */

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