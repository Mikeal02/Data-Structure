/*
 * DATE: April 5, 2026
 * PATTERN: Dynamic Programming, Array
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Enumerate all subarrays and multiply elements; track maximum product.
 * - TIME: O(n^2) or O(n^3) | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Prefix/suffix products with care for zeros—still need sign handling.
 * - TIME: O(n^2) naive extensions | SPACE: O(1)
 *
 * 3. OPTIMAL:
 * - Step 1: Track both current maximum and minimum ending here (negatives flip min to max).
 * - Step 2: Update answer from current_max each index.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: A negative number turns the smallest subproduct into the largest—track min and max together.
 */

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    // O(n^2)
    int max_product_subarray(vector<int>&arr)
    {
        int n=arr.size();
        int max_product=arr[0];
        for(int i=0;i<n;i++)
        {
            int current_prod=1;
            for(int j=i;j<n;j++)
            {
                current_prod*=arr[j];
                max_product=max(max_product,current_prod);
            }
        }
        return max_product;
    }

     int max_product_subarray(vector<int>&arr)
     {
        int current_max=arr[0];
        int current_min=arr[0];
        int res=arr[0];
        int n=arr.size();
        int current_prod=1;
        for(int i=1;i<n;i++)
        {
            if(arr[i]<0)
            swap(current_max,current_min);
            current_prod*=arr[i];
            current_max=max(arr[i],current_max*arr[i]);
            current_min=min(arr[i],current_min*arr[i]);

            res=max(res,current_max);

        }
        return res;
     }

};

int main()
{
    vector<int> arr={1,2,-3,0,-4,-5};
    Solution sol;
    int ans=sol.max_product_subarray(arr);
    cout<<ans;
    return 0;
}

