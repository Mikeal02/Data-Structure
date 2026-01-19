#include<bits/stdc++.h>
using namespace std;
class solution
{
    public:
    // optimal solution:O(n)

    void reverse(vector<int> & arr, int start, int end)
    {
        while(start<end)
        {
            swap(arr[start++],arr[end---]);
        }
    }
    void left_rotate_by_D(vector<int>& arr,int k, string direction)
    {
        int n=arr.size();
        if(n==0 || k==0)return;
        k%=n;
        if(direction=="left")
        {
        reverse(arr,0,k-1);
        reverse(arr,k,n-1);
        reverse(arr,0,n-1);
        }
        else
        {
            reverse(arr,0,n-1);
            reverse(arr,0,k-1);
            reverse(arr,k,n-1);
            
        }
    }
};
int main()
{
    vector<int> arr={1,2,3,4,5,6,7,8,9};
    solution sol;
    int n;
    cin>>n;
    string dir;
    cin>>str;
    sol.left_rotate_by_D(arr,n,dir);
    for(int x:arr)
    {
        cout<<x<<" ";
    }
    
}