/*
 * DATE: April 5, 2026
 * PATTERN: Array, Greedy / Right-to-left scan
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: For each index i, scan all elements to the right; i is a leader if nothing on the right is greater.
 * - TIME: O(n^2) | SPACE: O(n) for answer
 *
 * 2. BETTER:
 * - Step 1: Precompute suffix maximum array so each position checked in O(1).
 * - TIME: O(n) | SPACE: O(n) for suffix array
 *
 * 3. OPTIMAL:
 * - Step 1: Traverse from right to left; keep max_seen from the right; element is leader if it exceeds max_seen.
 * - Step 2: Last element is always a leader; reverse collected order if original left-to-right order is needed.
 * - TIME: O(n) | SPACE: O(1) extra besides output
 *
 * AHA-MOMENT: Leaders depend only on the maximum of the suffix—carry that max from the end in one pass.
 */

#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    // brute force approach: O(n^2),O(n)
    vector<int> leader_in_array(vector<int>& arr)
    {
        int n=arr.size();
        vector<int> ans;
        for(int i=0;i<n-1;i++)
        /*
         * APPROACH: For each element in the array (except the last), assume it is a leader. 
         * Then, for each element to its right, check if any is greater; if so, mark it not a leader and stop checking further.
         * If the assumption holds, add the element to the answer vector. This is the brute-force O(n^2) approach.
         * TIME: O(n^2) | SPACE: O(n)
         */
        {
            bool leader = true;
            for(int j = i + 1; j < n; j++)
            {
                if(arr[j] > arr[i])
                {
                    leader = false;
                    break;
                }
            }
            if(leader) ans.push_back(arr[i]);
        }
        }
        ans.push_back(arr[n-1]);
        return ans;
    }
    // optimal approach:O(n)
    vector<int> leader_in_array(vector<int>& arr)
    {
        /* 
         * APPROACH: Iterate from right to left in the array, maintaining the maximum seen so far (starting from the last element, which is always a leader).
         * For each element, if it is greater than the current maximum, add it to the answer vector and update the maximum.
         * At the end, reverse the answer vector to maintain the original order of leaders.
         * TIME: O(n) | SPACE: O(n)
         */
        int n=arr.size();
        vector<int>ans;
        if(arr.empty())return ans;
        int max_element=arr[n-1];
        ans.push_back(max_element);
        for(int i=n-2;i>=0;i--)
        {
            if(arr[i]>max_element)
            {
                ans.push_back(arr[i]);
                max_element=arr[i];
            }
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }

};
int main()
{
    vector<int> arr={10,22,12,3,0,6};
    Solution sol;
    vector<int> ans=sol.leader_in_array(arr);
    cout<<"The maximum subarray sum is:"<<endl;
    for(int x:ans)
    {
        cout<<x<<" ";
    }
    return 0;
}