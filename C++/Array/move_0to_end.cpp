/*
 * DATE: April 5, 2026
 * PATTERN: Two Pointers
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Build new list of non-zeros in order, append zeros to fill.
 * - TIME: O(n) | SPACE: O(n) auxiliary vector
 *
 * 2. BETTER:
 * - Step 1: Stable partition with extra array copy (two passes over copy).
 * - TIME: O(n) | SPACE: O(n)
 *
 * 3. OPTIMAL:
 * - Step 1: Slow pointer for next non-zero slot; fast pointer scans; swap non-zeros forward.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Partition the array in-place: the “write” index only advances when a non-zero is found.
 */

#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    // brute force solution: O(n+k),(k)
    void move_zero_to_end(vector<int>& arr)
    {
        int n=arr.size();
        vector<int> temp;
        for(int i:arr)
        {
            if(i!=0)
            {
                temp.push_back(i);
            }

        }
        for(int i=0;i<temp.size();i++)
        {
            arr[i]=temp[i];
        }
        for(int i=temp.size();i<n;i++)
        {
            arr[i]=0;
        }
   
    }

    // Optimal approach:O(2n)
    void move_zero_to_end(vector<int>& arr)
    {
        int n=arr.size();
        int j=0;
        for(int i=0;i<n;i++)
        {
            if(arr[i]==0)
            {
                j=i;
                break;
            }
        }
        for(int i=j+1;i<n;i++)       
        {
            if(arr[i]!=0)
            {
                swap(arr[i],arr[j]);
                j++;
            }
        } 
            
    }

};

int main()
{
    vector<int> arr={1,0,2,3,0,4,0,1};
    Solution sol;
     sol.move_zero_to_end(arr);
    for(int x:arr)
    {
        cout<<x<<" ";
    }
    return 0;
}