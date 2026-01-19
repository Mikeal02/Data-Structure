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
