/*
 * DATE: April 5, 2026
 * PATTERN: Two Pointers, In-place Array
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Insert elements into a set from sorted array, copy back (or check each against all prior).
 * - TIME: O(n log n) for set | SPACE: O(n)
 *
 * 2. BETTER:
 * - Step 1: Use set to collect unique in sorted order, return new length/size.
 * - TIME: O(n log n) | SPACE: O(n)
 *
 * 3. OPTIMAL:
 * - Step 1: Slow pointer i at last unique; fast j scans; when arr[j]!=arr[i], advance i and assign arr[i]=arr[j].
 * - Step 2: Return i+1 as new length.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Sorted duplicates are contiguous—one slow pointer “compresses” unique values in place.
 */

#include<bits/stdc++.h>
using namespace std;
class solution
{
    public:
    // Brute Force Solution: O(n),O(n)[Cause we used set to store elements]
    vector<int> remove_dup(vector<int> & arr)
    {
        set<int> st;
        for(int x:arr)
        {
            st.insert(x);

        }
        vector<int> ans(st.begin(),st.end());
        return ans;
    }

    // Optimal Solution:O(n)
    int remove_dup(vector<int>& arr)
    {
        if(arr.empty())return 0;
        int n=arr.size();
        int i=0;
        for(int j=1;j<n;j++)
        {
            if(arr[i]!=arr[j])
            {
                i++;
                arr[i]=arr[j];
            }
        }
        return i+1;
    }
};
int main()
{
    vector<int> arr={1,1,2,2,2,3,3};
    solution sol;
    int ans=sol.remove_dup(arr);
    cout<<ans;
}