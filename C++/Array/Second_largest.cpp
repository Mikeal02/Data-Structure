/*
 * DATE: April 5, 2026
 * PATTERN: Array Scan
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Find max, then find max among elements strictly less than first max (two passes).
 * - Step 2: Or compare all pairs for second largest.
 * - TIME: O(n^2) for pair approach | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Sort descending (or ascending) and take second distinct position.
 * - TIME: O(n log n) | SPACE: O(1) to O(n)
 *
 * 3. OPTIMAL:
 * - Step 1: One pass: maintain largest and second_largest; update when seeing larger or smaller-than-max but larger than second.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Track two leaders in one pass—no sort needed for second place.
 */

#include<bits/stdc++.h>
using namespace std;

// brute force solution: O(nlogn)
int Second_largest(vector<int>& arr)
{
    int n=arr.size();
    sort(arr.begin(),arr.end());
    return arr[n-2];
}

// optimal solution: O(n)
int Second_largest(vector<int> & arr)
{
    int n=arr.size();
    int maxi=arr[0];
    int maxi2=-1;
    for(int i=0;i<n;i++)
    {
        if(arr[i]>maxi)
        {
            maxi2=maxi;
            maxi=arr[i];

        }
        else if (arr[i]<maxi && arr[i]>maxi2)
        {
            maxi2=arr[i];
        }
    }
    return maxi2;
}


int main()
{
    vector<int> arr={2,3,4,5,22,65,23,12,53,65,75};
    int largest= second_element(arr);
    cout<<"This is the largest element: "<<largest;
    return 0;
}