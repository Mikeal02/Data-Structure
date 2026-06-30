/*
 * DATE: April 5, 2026
 * PATTERN: Sliding Window / Linear Scan
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: For each subarray, count ones and track maximum consecutive block.
 * - TIME: O(n^3) or O(n^2) | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Single pass from each index where arr[i]==1 as start—still redundant.
 * - TIME: O(n^2) worst | SPACE: O(1)
 *
 * 3. OPTIMAL:
 * - Step 1: One traversal; extend count while seeing 1, reset on 0, update max streak.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Longest run of 1s is found by one pass with a running counter reset at zeros.
 */

#include<bits/stdc++.h>
using namespace std;

// optimal solution: O(n)
int max_ones(vector<int>& ones)
{
    int len=ones.size();
    int j;
    for(int i=0;i<n;i++)
    {
        if(ones[i]==1)
        {
            j=i;
            break;
        }
    }
    int maxones=-1;
    int count=0;
    for(i=j;i<n;i++)
    {
        if(ones[i]==1)
        {
            count++;
            maxones=max(maxones,count);
        }
        else
        {
            count=0;
        }
    }
    return maxones;
}
int main()
{
    vector<int> ones={0,0,1,0,1,1,1,0,1,1};
    int maxones=max_ones(ones);
    cout<<"The maximum consecutive ones are:"<< maxones;
}