#include<bits/stdc++.h>
using namespace std;
class solution
{
    public:
    // Optimal Solution: O(n)
    bool is_sort(vector<int>&arr)
    {
        int n=arr.size();
        for(int i=1;i<n;i++)
        {
            if(arr[i]>arr[i-1])
            {
                continue;
            }
            else{

                return false;
            }
        }
        return true;
    }
};
int main()
{
    vector<int> arr={1,2,3,4,5};
    solution sol;
    bool answer=sol.is_sort(arr);
    cout<<answer<<endl;

}