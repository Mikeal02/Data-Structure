/*
 * DATE: April 5, 2026
 * PATTERN: Array Rotation
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Pop front and push to end using extra list operations or repeated single-step shifts.
 * - TIME: O(n) per rotation × rotations | SPACE: O(1) for one step
 *
 * 2. BETTER:
 * - Step 1: Copy to new array with shifted indices (i-k mod n).
 * - TIME: O(n) | SPACE: O(n)
 *
 * 3. OPTIMAL (rotate by 1):
 * - Step 1: Store first element, shift all elements left by one index, place stored value at end.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Left rotate by 1 is a single cyclic shift—one temp and one linear move.
 */

#include<bits/stdc++.h>
using namespace std;
class solution
{
    public:
    // optimal solution:O(n)
    void left_rotate_by_1(vector<int>& arr)
    {
        int first_element=arr[0];
        int n=arr.size();
        for(int i=1;i<arr.size();i++)
        {
            arr[i-1]=arr[i];
        }
        arr[n-1]=first_element;
    }
};

int main()
{
    vector<int> arr={1,2,3,4,5,6,7,8,9};
    solution sol;
    sol.left_rotate_by_1(arr);
    for(int x:arr)
    {
        cout<<x<<" ";
    }
    
}
