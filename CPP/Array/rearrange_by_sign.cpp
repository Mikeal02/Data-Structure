/*
 * DATE: April 5, 2026
 * PATTERN: Two Pointers, Array Partition
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Split into positives and negatives lists, then interleave by index rules.
 * - TIME: O(n) | SPACE: O(n) for extra vectors
 *
 * 2. BETTER:
 * - Step 1: Single pass to place positives at even and negatives at odd indices using separate write pointers (if counts balanced).
 * - TIME: O(n) | SPACE: O(n) for result array
 *
 * 3. OPTIMAL (structure in code):
 * - Step 1: Separate positive/negative buckets then merge in required alternating pattern.
 * - TIME: O(n) | SPACE: O(n) for output (in-place alternating with negatives/positives may need follow-up variants).
 *
 * AHA-MOMENT: Decouple “collect by sign” from “scatter to alternating slots”—two-phase keeps logic simple.
 */

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