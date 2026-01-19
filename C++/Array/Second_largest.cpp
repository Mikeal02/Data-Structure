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