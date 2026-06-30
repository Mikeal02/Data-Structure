/*
 * DATE: April 5, 2026
 * PATTERN: Array Scan / Selection
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Compare every element with every other to find the maximum (redundant comparisons).
 * - TIME: O(n^2) | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Sort ascending and take last element as maximum.
 * - TIME: O(n log n) | SPACE: O(1) to O(n) depending on sort
 *
 * 3. OPTIMAL:
 * - Step 1: One linear scan maintaining running maximum.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Maximum over a set is computable in one pass—sorting is unnecessary for finding the max alone.
 */

#include<bits/stdc++.h>
using namespace std;

// brute force solution: O(nlogn)
// sort the array
int largestelement(vector<int> & arr)
{
    int n=arr.size();
    sort(arr.begin(),arr.end());
    return arr[n-1];
}


// Optimal solution:O(n)
// Compare all the elements in the array
int largestelement(vector<int> & arr)
{
    int n=arr.size();
    int maxi=arr[0];
    int i=0;
    while (i<n)
    {
        if (arr[i]>maxi)
        {
            maxi=arr[i];
        }
        i++;
    }
    return maxi;
}



int main()
{
    vector<int> arr={2,3,4,5,22,65,23,12,53,65,75};
    int largest= largestelement(arr);
    cout<<"This is the largest element: "<<largest;
    return 0;
}