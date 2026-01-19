#include<bits/stdc++.h>
using namespace std;

// brute force solution: O(nlogn)
// sort the array
int largestelement(vector<int> & arr)
{
    int n=arr.size();
    sort(arr.begin(),arr.end())
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