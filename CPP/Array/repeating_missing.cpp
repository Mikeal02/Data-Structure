/*
 * DATE: April 5, 2026
 * PATTERN: Hashing / Counting
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: For each number 1..n, count occurrences by scanning the whole array each time.
 * - TIME: O(n^2) | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Frequency map or array of size n+1; increment per value; find value with count 2 and missing 0.
 * - TIME: O(n) | SPACE: O(n)
 *
 * 3. OPTIMAL (math variants exist):
 * - Step 1: Use counting array as in “better” when values in 1..n—same asymptotics, minimal overhead.
 * - Alternative: sum and sum of squares equations to derive repeating and missing (O(n) time, O(1) space).
 * - TIME: O(n) | SPACE: O(n) for frequency array here, or O(1) with algebraic method
 *
 * AHA-MOMENT: One duplicate and one missing show up as count 2 and count 0 in a 1..n index frequency table.
 */

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    vector<int> repeating_missing(vector<int> &arr)
    {
        int n=arr.size();
        vector<int> hash(n+1,0);
        vector<int>ans;
        for(int i=0;i<n;i++)n
        {
            hash[arr[i]]++;
        }
        for(int i=0;i<hash.size();i++)
        {
            if(hash[i]==2)
            {
                ans.push_back(i);
            }
            if(hash[i]==0)
            {
                ans.push_back(i);
            }
        }
        return ans;
    }
};

int main() {
    vector<int> nums = {3, 1, 2, 5, 4, 6, 7, 5};
    
    // Create an instance of Solution class
    Solution sol;

    vector<int> result = sol.repeating_missing(nums);
    
    // Print the repeating and missing numbers found
    cout << "The repeating and missing numbers are: {" << result[0] << ", " << result[1] << "}\n";
    
    return 0;
}