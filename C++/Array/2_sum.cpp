/*
 * DATE: April 5, 2026
 * PATTERN: Hashing, Two Pointers
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Try every pair (i, j) and check if arr[i] + arr[j] == target.
 * - Step 2: Return YES if any pair works, else NO.
 * - TIME: O(n^2) | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: One pass; for each arr[i], need (target - arr[i]) among indices before i.
 * - Step 2: Store visited values in an unordered_map for O(1) lookup.
 * - TIME: O(n) | SPACE: O(n) due to hash map
 *
 * 3. OPTIMAL (when array is sorted):
 * - Step 1: Sort (or start sorted), place pointers at both ends.
 * - Step 2: Move left/right based on whether current sum is below or above target.
 * - TIME: O(n log n) if sort needed, else O(n) | SPACE: O(1) for two pointers
 *
 * AHA-MOMENT: Complement lookup (target - x) turns pair search into O(n) with a map; two pointers work only when order is sorted.
 */

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    
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