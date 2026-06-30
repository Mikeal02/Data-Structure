/*
 * DATE: April 5, 2026
 * PATTERN: Linear Scan
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: For every i < j, verify arr[i] <= arr[j] (non-decreasing check all pairs).
 * - TIME: O(n^2) | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Sort a copy and compare to original, or compare adjacent after sort of index pairs.
 * - TIME: O(n log n) | SPACE: O(n)
 *
 * 3. OPTIMAL:
 * - Step 1: Single pass from index 1; if any arr[i] < arr[i-1], not sorted ascending.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Non-decreasing order is equivalent to every adjacent pair being valid—no need to compare all pairs.
 */

#include<bits/stdc++.h>
using namespace std;
class solution
{
    public:
    // Optimal Solution: O(n)
    bool is_sort(vector<int>&arr)
    {
        int n=arr.size();
        for(int i=1;i<n;i++)
        {
            if(arr[i]>arr[i-1])
            {
                continue;
            }
            else{

                return false;
            }
        }
        return true;
    }
};
int main()
{
    vector<int> arr={1,2,3,4,5};
    solution sol;
    bool answer=sol.is_sort(arr);
    cout<<answer<<endl;

}